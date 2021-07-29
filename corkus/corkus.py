from typing import Optional, Coroutine, Any
from corkus.utils.constants import TIMEOUT
from corkus.utils.request import CorkusRequest

from corkus.endpoints.network import NetworkEndpoint
from corkus.endpoints.player import PlayerEndpoint

class Corkus:
    """First-class interface for accessing Wynncraft API"""

    def __init__(self, *, timeout: Optional[int] = None) -> None:
        if timeout is None:
            timeout = TIMEOUT
        self.request = CorkusRequest(timeout)
        self.network = NetworkEndpoint(self)
        self.player = PlayerEndpoint(self)


    async def close(self) -> Coroutine[Any, Any, None]:
        return await self.request.session.close()
