from __future__ import annotations
from corkus.objects.playtime import PlayerPlaytime
from typing import TYPE_CHECKING, Union, Optional

from .base_player import BasePlayer
from .leaderboard_partial_member import LeaderboardPartialMember
from .partial_guild import PartialGuild

if TYPE_CHECKING:
    from .player import Player

class LeaderboardPlayer(BasePlayer):
    """Diffrent version of :py:class:`Player` returned by :py:class:`LeaderboardEndpoint <corkus.endpoints.LeaderboardEndpoint>`."""
    @property
    def username(self) -> str:
        """Minecraft username of player."""
        return self._attributes.get("name", "")

    @property
    def playtime(self) -> PlayerPlaytime:
        """Time that player spent on wynncraft servers."""
        return PlayerPlaytime(self._attributes.get("minPlayed", 0))

    @property
    def pvp_kills(self) -> int:
        """Total player killed in `The Nether <https://wynncraft.fandom.com/wiki/The_Nether>`_."""
        return self._attributes.get("kills", 0)

    @property
    def total_combat_level(self) -> int:
        """Combined combat level across all classes."""
        return self._attributes.get("level", 0)

    @property
    def total_xp(self) -> int:
        """Total collected combat XP points across all classes."""
        return self._attributes.get("level", 0)

    @property
    def position(self) -> int:
        """This player possition in players leaderboard."""
        return self._attributes.get("num", 0)

    @property
    def member(self) -> Union[LeaderboardPartialMember, None]:
        """Partial representation of player in the guild."""
        if self._attributes.get("guildTag") is None:
            return None
        else:
            return LeaderboardPartialMember(
                corkus = self._corkus,
                uuid = self.uuid,
                username = self.username,
                guild = self.guild,
                tag = self._attributes.get("guildTag")
            )

    @property
    def guild(self) -> Union[PartialGuild, None]:
        """Partial information about player's guild."""
        if self._attributes.get("guild") is None:
            return None
        else:
            return PartialGuild(self._corkus, self._attributes.get("guild"))

    async def fetch(self, timeout: Optional[int] = None) -> Player:
        """Fetch information about this player from Players API.

        .. include:: ../note_api_call.rst

        :param timeout: Optionally override default timeout.
        """
        return await self._corkus.player.get(self.uuid, timeout)

    def __repr__(self) -> str:
        return f"<LeaderboardPlayer username={self.username!r}>"
