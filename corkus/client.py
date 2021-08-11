from __future__ import annotations
from typing import Optional, Coroutine, Any, TYPE_CHECKING
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

if TYPE_CHECKING:
    from .utils.ratelimit import RateLimiter
    from aiohttp import ClientSession

class Corkus:
    """First-class interface for accessing Wynncraft API"""

    def __init__(self, *,
        timeout: Optional[int] = None,
        session: Optional[ClientSession] = None,
        ratelimit_enable: Optional[bool] = True,
        cache_enable: Optional[bool] = True,
    ) -> None:
        if timeout is None:
            timeout = TIMEOUT
        self._request = CorkusRequest(timeout, session, ratelimit_enable, cache_enable)

    async def __aenter__(self) -> "Corkus":
        """Async enter"""
        return self

    async def __aexit__(self, *exc_info) -> None:
        """Async exit"""
        await self.close()

    @property
    def request(self) -> CorkusRequest:
        """Access request module to make direct API calls or get ratelimit an cache information
        .. note::
            Directly making API calls is reserver for advanced users only
            If there is an endpoint that you can't normall access using library,
            please `create a issue <https://github.com/MrBartusek/corkus.py/issues/new>`_
        """
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
        return await self.request.session.close()
