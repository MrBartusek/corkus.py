from __future__ import annotations
from typing import Optional, TYPE_CHECKING
from corkus.errors import CorkusException
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

class Corkus:
    """Represents a API client used for accessing wynncraft resources.

    A number of options can be passed to the :py:class:`Corkus`.
    For full lust of configuration options see: :ref:`configuration`."""

    def __init__(self, *,
        timeout: Optional[int] = 60,
        disable_ratelimit: Optional[bool] = False,
        disable_cache: Optional[bool] = False,
    ) -> None:
        self._request = CorkusRequest(timeout, disable_ratelimit, disable_cache)
        self._initialized = False

    async def start(self, api_key: Optional[str] = None) -> None:
        """Initialize this Corkus instance. Client needs to be initialized to make any API calls."""
        await self._request.start(api_key)
        self._initialized = True

    async def __aenter__(self) -> "Corkus":
        """Async enter."""
        await self.start()
        return self

    async def __aexit__(self, *exc_info) -> None:
        """Async exit."""
        await self.close()

    @property
    def player(self) -> PlayerEndpoint:
        """General statistics of wynncraft players."""
        self._checkInitialized()
        return PlayerEndpoint(self, self._request)

    @property
    def guild(self) -> GuildEndpoint:
        """Information about server guilds."""
        self._checkInitialized()
        return GuildEndpoint(self, self._request)

    @property
    def network(self) -> NetworkEndpoint:
        """Wynncraft Network specific routes like list of all players."""
        self._checkInitialized()
        return NetworkEndpoint(self, self._request)

    @property
    def territory(self) -> TerritoryEndpoint:
        """Information about teritories."""
        self._checkInitialized()
        return TerritoryEndpoint(self, self._request)

    @property
    def search(self) -> SearchEndpoint:
        """Search for guild and players."""
        self._checkInitialized()
        return SearchEndpoint(self, self._request)

    @property
    def item(self) -> ItemEndpoint:
        """Regular (not crafted) items database."""
        self._checkInitialized()
        return ItemEndpoint(self, self._request)

    @property
    def recipe(self) -> RecipeEndpoint:
        """Crafted items statistics and recipes."""
        self._checkInitialized()
        return RecipeEndpoint(self, self._request)

    @property
    def ingredient(self) -> IngredientEndpoint:
        """Information about ingredients."""
        self._checkInitialized()
        return IngredientEndpoint(self, self._request)

    @property
    def leaderboard(self) -> LeaderboardEndpoint:
        """Leaderboards of best players and guilds."""
        self._checkInitialized()
        return LeaderboardEndpoint(self, self._request)

    def _checkInitialized(self):
        if not self._initialized:
            raise CorkusException("Corkus is not initialized. Use corkus.start() before making any requests.")

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

class RateLimit:
    """Current ratelimit information for a Corkus instance. You should consider
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

    def __repr__(self) -> str:
        return f"<RateLimit total={self.total} remaining={self.remaining} reset={self.reset}>"
