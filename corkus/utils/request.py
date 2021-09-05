from __future__ import annotations
from os import error
from typing import Optional
from enum import Enum
import asyncio
from aiohttp.client import ClientSession, ClientResponse
import copy
import logging

from .cache import CorkusCache
from .ratelimit import RateLimiter
from corkus.version import __version__
from corkus.errors import BadRequest, WynncraftServerError, RatelimitExceeded, HTTPError, CorkusTimeoutError

logger = logging.getLogger("corkus.request")

class APIVersion(Enum):
    V1 = "https://api.wynncraft.com/public_api.php?action="
    V2 = "https://api.wynncraft.com/v2/"

class CorkusRequest:
    """CorkusRequest is a internal overlay over aiohttp to simplify API calls."""

    def __init__(self,
        timeout: Optional[int] = 0,
        api_key: Optional[str] = None,
        session: Optional[ClientSession] = None,
        ratelimit_enable: Optional[bool] = True,
        cache_enable: Optional[bool] = True,
    ) -> None:
        self.ratelimit = RateLimiter()
        self.cache = CorkusCache()
        self.ratelimit_enable = ratelimit_enable
        self.cache_enable = cache_enable

        self._session = session
        self.timeout = timeout
        if session is None:
            headers = {
                "User-Agent": f"Corkus.py/{__version__}",
                "Content-Type": "application/json"
            }
            if api_key is not None:
                headers["apikey"] = api_key
            self._session = ClientSession(headers = headers)

    async def get(self, version: APIVersion, parameters: str, timeout: Optional[int]) -> dict:
        url = version.value + parameters

        if self.cache_enable:
            cache_element = self.cache.get(url)
            if cache_element:
                return copy.copy(cache_element.content)

        if self.ratelimit_enable:
            await self.ratelimit.limit()

        try:
            response = await self._session.get(url, timeout = timeout or self.timeout)
            data = await response.json()
        except asyncio.TimeoutError:
            raise CorkusTimeoutError(timeout, error)

        self.ratelimit.update(response.headers)
        self._fix_status_codes(data, response)

        if 200 <= response.status < 400:
            self.cache.add(url, response.headers, data)
            return copy.copy(data)

        elif response.status >= 500:
            raise WynncraftServerError(response)
        elif response.status >= 429:
            raise RatelimitExceeded(response)
        elif response.status >= 400:
            raise BadRequest(response)
        else:
            raise HTTPError(response)

    async def close(self) -> None:
        return await self._session.close()

    def _fix_status_codes(self, data: dict, response: ClientResponse) -> None:
        """Fix endpoints that return wrong status codes."""

        # https://github.com/Wynncraft/WynncraftAPI/issues/63
        # and other similar
        if data.get("error") is not None and response.status != 400:
            logger.debug(f"Got error field but status code is {response.status}- changing to: 400")
            response.status = 400

        elif data.get("status", 200) != response.status:
            status_field = data.get("status", 200)
            new_status = max(data.get("status", 200), response.status)
            logger.debug(f"Status field [{status_field}] is diffrent than status code [{response.status}] - changing to: {new_status}")
            response.status = new_status
