from __future__ import annotations
from typing import TYPE_CHECKING, Coroutine, Any
from .base_guild import BaseGuild

if TYPE_CHECKING:
    from .guild import Guild

class LeaderboardGuild(BaseGuild):
    @property
    def members_count(self) -> int:
        """List of all guild members"""
        return self._attributes.get("membersCount", 0)

    @property
    def total_xp(self) -> int:
        """Total sum of all xp points collected by this guild"""
        return self._attributes.get("xp", 0)

    @property
    def position(self) -> int:
        """This guild possition in guilds leaderboard"""
        return self._attributes.get("num", 0)

    @property
    def war_count(self) -> int:
        """Total wars performed by this guild"""
        return self._attributes.get("warCount", 0)

    async def fetch(self) -> Coroutine[Any, Any, Guild]:
        """Fetch information about this guild from Guilds API"""
        return await self._corkus.guild.get(self.name)

    def __repr__(self) -> str:
        return f"<Guild tag={self.tag!r} name={self.name!r}>"
