from __future__ import annotations
from corkus.objects.playtime import PlayerPlaytime
from typing import TYPE_CHECKING, Union

from .base_player import BasePlayer
from .leaderboard_partial_member import LeaderboardPartialMember
from .partial_guild import PartialGuild

if TYPE_CHECKING:
    from .player import Player

class LeaderboardPlayer(BasePlayer):
    @property
    def username(self) -> str:
        """Minecraft username of player"""
        return self.attributes.get("name", "")

    @property
    def playtime(self) -> PlayerPlaytime:
        """Time that player spent on wynncraft servers"""
        return PlayerPlaytime(self.attributes.get("minPlayed", 0))

    @property
    def pvp_kills(self) -> int:
        """Total player killed in [The Nether](https://wynncraft.fandom.com/wiki/The_Nether)"""
        return self.attributes.get("kills", 0)

    @property
    def total_combat_level(self) -> int:
        """Combined combat level across all classes"""
        return self.attributes.get("level", 0)

    @property
    def total_xp(self) -> int:
        """Total collected combat XP points across all classes"""
        return self.attributes.get("level", 0)

    @property
    def position(self) -> int:
        """This player possition in players leaderboard"""
        return self.attributes.get("num", 0)

    @property
    def member(self) -> Union[LeaderboardPartialMember, None]:
        """Partial representation of player in the guild"""
        if self.attributes.get("guildTag") is None:
            return None
        else:
            return LeaderboardPartialMember(
                corkus = self.corkus,
                uuid = self.uuid,
                username = self.username,
                guild = self.guild,
                tag = self.attributes.get("guildTag")
            )

    @property
    def guild(self) -> Union[PartialGuild, None]:
        """Partial information about player's guild"""
        if self.attributes.get("guild") is None:
            return None
        else:
            return PartialGuild(self.corkus, self.attributes.get("guild"))

    async def fetch(self) -> Player:
        """Fetch information about this player from Players API"""
        return await self.corkus.player.get(self.uuid)

    def __repr__(self) -> str:
        return f"<LeaderboardPlayer username={self.username!r}>"
