from __future__ import annotations
from typing import TYPE_CHECKING, Optional
from .base_guild import BaseGuild

if TYPE_CHECKING:
    from .guild import Guild

class LeaderboardGuild(BaseGuild):
    """Diffrent version of :py:class:`Guild` returned by :py:class:`LeaderboardEndpoint <corkus.endpoints.LeaderboardEndpoint>`."""
    @property
    def members_count(self) -> int:
        """Count of guild members, to access full list use :py:func:`fetch`."""
        return self._attributes.get("membersCount", 0)

    @property
    def total_xp(self) -> int:
        """Total sum of all xp points collected by this guild."""
        return self._attributes.get("xp", 0)

    @property
    def position(self) -> int:
        """This guild possition in guilds leaderboard."""
        return self._attributes.get("num", 0)

    @property
    def war_count(self) -> int:
        """Number of wars the guild has done, including failed ones."""
        return self._attributes.get("warCount", 0)

    async def fetch(self, timeout: Optional[int] = None) -> Guild:
        """Fetch information about this guild from Guilds API.

        .. include:: ../note_api_call.rst

        :param timeout: Optionally override default timeout.
        """
        return await self._corkus.guild.get(self.name, timeout)

    def __repr__(self) -> str:
        return f"<Guild tag={self.tag!r} name={self.name!r}>"
