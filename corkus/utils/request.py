from __future__ import annotations
from corkus.utils.cache import CorkusCache
from aiohttp.client import ClientSession, ClientTimeout
from corkus.utils.ratelimit import RateLimiter
from typing import Optional
from corkus.version import __version__
import copy

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

    async def get(self, url: str) -> dict:
        cache_element = self._cache.get(url)
        if cache_element:
            return copy.copy(cache_element.content)

        await self._ratelimit.limit()
        resp = await self._session.get(url)
        data = await resp.json()
        self._ratelimit.update(resp.headers)
        data = self._prepare_data(data)
        self._cache.add(url, resp.headers, data)
        return copy.copy(data)

    def _prepare_data(self, data: dict) -> dict:
        """Reduce to data object for v2 endpoints"""
        if data.get("data") is not None:
            data = data.get("data")
            if len(data) == 1:
                data = data[0]
        return data
