from typing import Optional, Coroutine, Any
from corkus.utils.constants import TIMEOUT
from corkus.utils.request import CorkusRequest

from corkus.endpoints.network import NetworkEndpoint
from corkus.endpoints.player import PlayerEndpoint
from corkus.endpoints.guild import GuildEndpoint
from corkus.endpoints.territory import TerritoryEndpoint

class Corkus:
    """First-class interface for accessing Wynncraft API"""

    def __init__(self, *, timeout: Optional[int] = None) -> None:
        if timeout is None:
            timeout = TIMEOUT
        self.request = CorkusRequest(timeout)

    @property
    def network(self) -> NetworkEndpoint:
        return NetworkEndpoint(self)

    @property
    def player(self) -> PlayerEndpoint:
        return PlayerEndpoint(self)

    @property
    def guild(self) -> GuildEndpoint:
        return GuildEndpoint(self)

    @property
    def territory(self) -> TerritoryEndpoint:
        return TerritoryEndpoint(self)

    async def close(self) -> Coroutine[Any, Any, None]:
        return await self.request.session.close()
