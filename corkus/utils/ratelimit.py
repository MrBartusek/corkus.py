from __future__ import annotations
from multidict import CIMultiDictProxy
import time
import logging
import asyncio

logger = logging.getLogger("corkus.ratelimit")

class RateLimiter:
    def __init__(self, enable: bool) -> None:
        self._total = 180
        self._remaining = 180
        self._reset = 0
        self._enabled = enable

    @property
    def enabled(self) -> bool:
        """Is ratelimiter enabled"""
        return self._enabled

    @property
    def total(self) -> int:
        """Total amount of requests that you can make to the API per minute"""
        return self._total

    @property
    def remaining(self) -> int:
        """Total amount of requests left per that minute"""
        if self.reset < 0:
            return self.total
        else:
            return self._remaining

    @property
    def reset(self) -> int:
        """Remaining seconds to when limit will reset to :py:atrr:`~total`"""
        return self._reset - int(time.time())

    async def limit(self) -> None:
        """Delay execution when hitting ratelimit"""
        if self.remaining < 3 and self.enabled:
            logger.info(f"You are being ratelimited, waiting for {self.reset}s")
            await asyncio.sleep(self.reset)

    def update(self, headers: CIMultiDictProxy[str]) -> None:
        """Update current ratelimit information using response headers"""
        self._total = int(headers.get("ratelimit-limit", 180))
        self._remaining = int(headers.get("ratelimit-remaining", 180))
        self._reset = int(time.time()) + int(headers.get("ratelimit-reset", 0))

    def __repr__(self) -> str:
        return f"<RateLimiter remaining={self.remaining} total={self.total} reset={self.reset}>"
