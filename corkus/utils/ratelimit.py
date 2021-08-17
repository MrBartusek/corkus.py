from __future__ import annotations
import time
import logging
import asyncio

logger = logging.getLogger("corkus.ratelimit")

class RateLimiter:
    def __init__(self) -> None:
        self._total = 180
        self._remaining = 180
        self._reset = 0

    @property
    def total(self) -> int:
        return self._total

    @property
    def remaining(self) -> int:
        if self.reset < 0:
            return self.total
        else:
            return self._remaining

    @property
    def reset(self) -> int:
        return self._reset - int(time.time())

    async def limit(self) -> None:
        if self.remaining <= 1:
            logger.info(f"You are being ratelimited, waiting for {self.reset}s")
            await asyncio.sleep(self.reset)

    def update(self, headers: dict) -> None:
        self._total = int(headers.get("ratelimit-limit", 180))
        self._remaining = int(headers.get("ratelimit-remaining", 180))
        self._reset = int(time.time()) + int(headers.get("ratelimit-reset", 0))
