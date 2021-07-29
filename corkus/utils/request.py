from aiohttp.client import ClientSession, ClientTimeout
from typing import Optional
from corkus.version import __version__

class CorkusRequest:
    def __init__(self, timeout: int = 0, session: Optional[ClientSession] = None) -> None:
        self.session = session
        if session is None:
            self.session = ClientSession(
                timeout = ClientTimeout(total = timeout),
                headers = {
                    "User-Agent": f"Corkus.py/{__version__}",
                    "Content-Type": "application/json"
                }
            )

    async def get(self, url) -> dict:
        resp = await self.session.get(url)
        data = await resp.json()
        return data
