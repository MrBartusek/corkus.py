from typing import Optional, Coroutine, Any
from corkus.utils.constants import TIMEOUT
from corkus.utils.request import CorkusRequest

from corkus.endpoints.network import NetworkEndpoint
from corkus.endpoints.player import PlayerEndpoint
from corkus.endpoints.guild import GuildEndpoint
from corkus.endpoints.territory import TerritoryEndpoint
from corkus.endpoints.search import SearchEndpoint

class Corkus:
    """First-class interface for accessing Wynncraft API"""

    def __init__(self, *, timeout: Optional[int] = None) -> None:
        if timeout is None:
            timeout = TIMEOUT
        self.request = CorkusRequest(timeout)

    @property
    def network(self) -> NetworkEndpoint:
        """Wynncraft Network specific routes like list of all players"""
        return NetworkEndpoint(self)

    @property
    def player(self) -> PlayerEndpoint:
        """Statistics of players"""
        return PlayerEndpoint(self)

    @property
    def guild(self) -> GuildEndpoint:
        """Information about server guilds"""
        return GuildEndpoint(self)

    @property
    def territory(self) -> TerritoryEndpoint:
        """Information about teritories"""
        return TerritoryEndpoint(self)

    @property
    def search(self) -> SearchEndpoint:
        """Search for guild and players"""
        return SearchEndpoint(self)

    async def close(self) -> Coroutine[Any, Any, None]:
        """End the corkus client when it's not needed anymore"""
        return await self.request.session.close()
