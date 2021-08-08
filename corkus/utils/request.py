from .ratelimit import RateLimiter
from aiohttp.client import ClientSession, ClientTimeout
from typing import Optional
from corkus.version import __version__

class CorkusRequest:
    def __init__(self, timeout: int = 0, session: Optional[ClientSession] = None) -> None:
        self._session = session
        self.ratelimit = RateLimiter()
        if session is None:
            self._session = ClientSession(
                timeout = ClientTimeout(total = timeout),
                headers = {
                    "User-Agent": f"Corkus.py/{__version__}",
                    "Content-Type": "application/json"
                }
            )

    async def get(self, url) -> dict:
        await self.ratelimit.limit()
        resp = await self._session.get(url)
        data = await resp.json()
        self.ratelimit.update(resp.headers)

        # For V2 Endpoints
        if data.get("data") is not None:
            data = data.get("data")
            if len(data) == 1:
                data = data[0]

        return data
