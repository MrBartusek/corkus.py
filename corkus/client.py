from __future__ import annotations
from typing import Optional, TYPE_CHECKING
from corkus.utils.request import CorkusRequest

from corkus.endpoints import (
    NetworkEndpoint,
    PlayerEndpoint,
    GuildEndpoint,
    TerritoryEndpoint,
    SearchEndpoint,
    IngredientEndpoint,
    LeaderboardEndpoint,
    RecipeEndpoint,
    ItemEndpoint
)

if TYPE_CHECKING:
    from aiohttp import ClientSession

class RateLimit:
    """Current ratelimit information for a Corkus instance. You should considier
    these values as a information rather than use them in regulating your requests
    since, Corkus have a ratelimit system in place.
    """
    def __init__(self, total: int, remaining: int, reset: int) -> None:
        self._total = total
        self._remaining = remaining
        self._reset = reset

    @property
    def total(self) -> int:
        """Total number of requests that user can send per minute under provided
        API key or IP if one is not provided."""
        return self._total

    @property
    def remaining(self) -> int:
        """Total number of requests left that user can send for that minute
        (:py:attr:`total` - used)."""
        return self._remaining

    @property
    def reset(self) -> int:
        """Number of seconds left until this minute ends and thus ratelimit
        is restored back to :py:attr:`total`."""
        return self._reset

class Corkus:
    """First-class interface for accessing Wynncraft API.

    For configuration options see: :ref:`configuration`."""

    def __init__(self, *,
        api_key: Optional[str] = None,
        timeout: Optional[int] = 30,
        session: Optional[ClientSession] = None,
        ratelimit_enable: Optional[bool] = True,
        cache_enable: Optional[bool] = True,
    ) -> None:
        self._api_key = api_key
        self._request = CorkusRequest(timeout, api_key, session, ratelimit_enable, cache_enable)

    async def __aenter__(self) -> "Corkus":
        """Async enter."""
        return self

    async def __aexit__(self, *exc_info) -> None:
        """Async exit."""
        await self.close()

    @property
    def player(self) -> PlayerEndpoint:
        """General statistics of wynncraft players."""
        return PlayerEndpoint(self, self._request)

    @property
    def guild(self) -> GuildEndpoint:
        """Information about server guilds."""
        return GuildEndpoint(self, self._request)

    @property
    def network(self) -> NetworkEndpoint:
        """Wynncraft Network specific routes like list of all players."""
        return NetworkEndpoint(self, self._request)

    @property
    def territory(self) -> TerritoryEndpoint:
        """Information about teritories."""
        return TerritoryEndpoint(self, self._request)

    @property
    def search(self) -> SearchEndpoint:
        """Search for guild and players."""
        return SearchEndpoint(self, self._request)

    @property
    def item(self) -> ItemEndpoint:
        """Regular (not crafted) items database."""
        return ItemEndpoint(self, self._request)

    @property
    def recipe(self) -> RecipeEndpoint:
        """Crafted items statistics and recipes."""
        return RecipeEndpoint(self, self._request)

    @property
    def ingredient(self) -> IngredientEndpoint:
        """Information about ingredients."""
        return IngredientEndpoint(self, self._request)

    @property
    def leaderboard(self) -> LeaderboardEndpoint:
        """Leaderboards of best players and guilds."""
        return LeaderboardEndpoint(self, self._request)

    @property
    def rate_limit(self) -> RateLimit:
        """Current ratelimit information for this Corkus instance."""
        return RateLimit(
            total = self._request.ratelimit.total,
            remaining = self._request.ratelimit.remaining,
            reset = self._request.ratelimit.reset
        )

    async def close(self) -> None:
        """End the corkus client when it's not needed anymore."""
        return await self._request.close()
