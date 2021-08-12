from __future__ import annotations
from typing import Optional, TYPE_CHECKING
from corkus.utils.constants import TIMEOUT
from corkus.utils.request import CorkusRequest

from corkus.endpoints import (
    NetworkEndpoint,
    PlayerEndpoint,
    GuildEndpoint,
    TerritoryEndpoint,
    SearchEndpoint,
    IngredientEndpoint,
    LeaderboardEndpoint,
    RecipeEndpoint
)

if TYPE_CHECKING:
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
        """Async enter."""
        return self

    async def __aexit__(self, *exc_info) -> None:
        """Async exit."""
        await self.close()

    @property
    def network(self) -> NetworkEndpoint:
        """Wynncraft Network specific routes like list of all players."""
        return NetworkEndpoint(self)

    @property
    def player(self) -> PlayerEndpoint:
        """Statistics of players."""
        return PlayerEndpoint(self)

    @property
    def guild(self) -> GuildEndpoint:
        """Information about server guilds."""
        return GuildEndpoint(self)

    @property
    def territory(self) -> TerritoryEndpoint:
        """Information about teritories."""
        return TerritoryEndpoint(self)

    @property
    def search(self) -> SearchEndpoint:
        """Search for guild and players."""
        return SearchEndpoint(self)

    @property
    def ingredient(self) -> IngredientEndpoint:
        """Information about ingredients."""
        return IngredientEndpoint(self)

    @property
    def leaderboard(self) -> LeaderboardEndpoint:
        """Leaderboards of best players and guilds."""
        return LeaderboardEndpoint(self)

    @property
    def recipe(self) -> RecipeEndpoint:
        """Crafted items statistics and recipes."""
        return RecipeEndpoint(self)

    @property
    def request(self) -> CorkusRequest:
        """Access internal request module to make direct API calls or
        get ratelimit and cache information."""
        return self._request

    async def close(self) -> None:
        """End the corkus client when it's not needed anymore."""
        return await self.request.session.close()
