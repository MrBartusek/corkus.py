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
        """Wynncraft Network specific routes

        - list of servers
        - sum of online players
        """
        return NetworkEndpoint(self)

    @property
    def player(self) -> PlayerEndpoint:
        """Statistics of players

        - player statistics
        - get uuid of player
        """
        return PlayerEndpoint(self)

    @property
    def guild(self) -> GuildEndpoint:
        """Information about server guilds

        - stats of specific guild
        - list of all guild
        """
        return GuildEndpoint(self)

    @property
    def territory(self) -> TerritoryEndpoint:
        """Information about teritories

        - list all teritories
        """
        return TerritoryEndpoint(self)

    async def close(self) -> Coroutine[Any, Any, None]:
        """End the corkus client when it's not needed anymore"""
        return await self.request.session.close()
