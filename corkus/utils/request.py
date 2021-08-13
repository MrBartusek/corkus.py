from __future__ import annotations
from corkus.version import __version__
from typing import List, Optional, Union
import copy

from corkus.utils.cache import CorkusCache
from aiohttp.client import ClientSession, ClientTimeout, ClientResponse
from corkus.utils.ratelimit import RateLimiter
from corkus.errors import BadRequest, WynncraftServerError, RatelimitExceeded, HTTPException

class CorkusRequest:
    """CorkusRequest is a internal overlay over aiohttp to simplify APi calls"""

    def __init__(self,
        timeout: Optional[int] = 0,
        session: Optional[ClientSession] = None,
        ratelimit_enable: Optional[bool] = True,
        cache_enable: Optional[bool] = True,
    ) -> None:
        self._session = session
        self._ratelimit = RateLimiter(ratelimit_enable)
        self._cache = CorkusCache(cache_enable)
        if session is None:
            self._session = ClientSession(
                timeout = ClientTimeout(total = timeout),
                headers = {
                    "User-Agent": f"Corkus.py/{__version__}",
                    "Content-Type": "application/json"
                }
            )

    @property
    def session(self) -> ClientSession:
        return self._session

    @property
    def ratelimit(self) -> RateLimiter:
        return self._ratelimit

    @property
    def cache(self) -> CorkusCache:
        return self._cache

    async def get(self, url: str) -> Union[dict, List[dict], List[str]]:
        """ Send HTTP GET to given URL.

        .. note::
            Directly making API calls is reserver for advanced users only,
            If there is an endpoint that you can't normall access using library,
            please `create a issue <https://github.com/MrBartusek/corkus.py/issues/new>`_."""

        cache_element = self._cache.get(url)
        if cache_element:
            return copy.copy(cache_element.content)

        await self._ratelimit.limit()
        response = await self._session.get(url)
        data = await response.json()
        self._ratelimit.update(response.headers)
        self._fix_status_codes(data, response)

        if 200 <= response.status < 400:
            data = self._prepare_data(data)
            self._cache.add(url, response.headers, data)
            return copy.copy(data)

        elif response.status >= 500:
            raise WynncraftServerError(response)
        elif response.status >= 429:
            raise RatelimitExceeded(response)
        elif response.status >= 400:
            raise BadRequest(response)
        else:
            raise HTTPException(response)

    def _prepare_data(self, data):
        """Reduce to data object for v2 endpoints"""
        if data.get("data") is not None:
            data = data.get("data")
            if len(data) == 1:
                data = data[0]
        return data

    def _fix_status_codes(self, data: dict, response: ClientResponse) -> None:
        """Fix endpoints that return wrong status codes"""

        # https://github.com/Wynncraft/WynncraftAPI/issues/63
        # and other similar
        if data.get("error") is not None:
            response.status = 400
