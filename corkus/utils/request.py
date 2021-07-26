from aiohttp.client import ClientSession, ClientTimeout, ClientResponse
from corkus.version import __version__

class CorkusRequest:
    def __init__(self, timeout) -> None:
        self.session = ClientSession(
            timeout = ClientTimeout(total = timeout),
            headers = { "User-Agent": f"Corkus.py/{__version__}" }
        )

    async def get(self, url) -> ClientResponse:
        resp = await self.session.get(url)
        data = await resp.json()
        return data
