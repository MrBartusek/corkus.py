from typing import Optional, Coroutine, Any
from corkus.utils.constants import TIMEOUT
from corkus.utils.request import CorkusRequest

from corkus.endpoints.network import NetworkEndpoint
from corkus.endpoints.player import PlayerEndpoint
from corkus.endpoints.guild import GuildEndpoint
from corkus.endpoints.territory import TerritoryEndpoint
from corkus.endpoints.search import SearchEndpoint
from corkus.endpoints.ingredient import IngredientEndpoint
from corkus.endpoints.leaderboard import LeaderboardEndpoint
from corkus.endpoints.recipe import RecipeEndpoint

class Corkus:
    """First-class interface for accessing Wynncraft API"""

    def __init__(self, *, timeout: Optional[int] = None) -> None:
        if timeout is None:
            timeout = TIMEOUT
        self._request = CorkusRequest(timeout)

    async def __aenter__(self) -> "Corkus":
        """Async enter"""
        return self

    async def __aexit__(self, *exc_info) -> None:
        """Async exit"""
        await self.close()

    @property
    def request(self) -> CorkusRequest:
        """Access request module to make direct API calls"""
        return self._request

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

    @property
    def ingredient(self) -> IngredientEndpoint:
        """Information about ingredients"""
        return IngredientEndpoint(self)

    @property
    def leaderboard(self) -> LeaderboardEndpoint:
        """Leaderboards of best players and guilds"""
        return LeaderboardEndpoint(self)

    @property
    def recipe(self) -> RecipeEndpoint:
        """Crafted items statistics and recipes"""
        return RecipeEndpoint(self)

    async def close(self) -> Coroutine[Any, Any, None]:
        """End the corkus client when it's not needed anymore"""
        return await self.request._session.close()
