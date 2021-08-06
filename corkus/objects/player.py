from corkus.objects.playtime import PlayerPlaytime
from typing import Union
import iso8601
from datetime import datetime

from .base_player import BasePlayer
from .partial_member import PartialMember
from .partial_guild import PartialGuild
from .member import GuildRank
from .player_status import PlayerStatus
from .player_statistics import PlayerStatistics
from .player_class import PlayerClass

class Player(BasePlayer):
    @property
    def username(self) -> str:
        """Minecraft username of player"""
        return self.attributes.get("username", "")

    @property
    def join_date(self) -> datetime:
        """Date and time when player joined Wynncraft first time"""
        return iso8601.parse_date(self.attributes.get("meta", {}).get("firstJoin", "1970"))

    def last_online(self) -> datetime:
        """Date and time when player was last seen online"""
        if self.status.online:
            return datetime.utcnow()
        else:
            return iso8601.parse_date(self.attributes.get("meta", {}).get("lastJoin", "1970"))

    @property
    def status(self) -> PlayerStatus:
        """Information about player's current online status"""
        return PlayerStatus(self.corkus, self.attributes.get("meta", {}).get("location", {}))

    @property
    def playtime(self) -> PlayerPlaytime:
        """Time that player spent on wynncraft servers"""
        return PlayerPlaytime(self.attributes.get("meta", {}).get("playtime", 0))

    @property
    def classes(self):
        """All of the player's classes"""
        return [PlayerClass(self.corkus, c) for c in self.attributes.get("classes", {})]

    @property
    def member(self) -> Union[PartialMember, None]:
        """Partial representation of player in the guild"""
        if self.attributes.get("guild", {}).get("name", None) is None:
            return None
        else:
            return PartialMember(
                corkus = self.corkus,
                uuid = self.uuid,
                username = self.username,
                guild = self.guild,
                rank = GuildRank(self.attributes.get("guild", {}).get("rank", "RECRUIT"))
            )

    @property
    def guild(self) -> Union[PartialGuild, None]:
        """Partial information about player's guild"""
        if self.attributes.get("guild", {}).get("name", None) is None:
            return None
        else:
            return PartialGuild(self.corkus, self.attributes.get("guild", {}).get("name", ""))

    @property
    def statistics(self):
        """General statistics across all classes"""
        return PlayerStatistics(self.corkus, self.attributes.get("global", {}))

    @property
    def ranking(self):
        raise NotImplementedError

    def __repr__(self) -> str:
        return f"<Player username={self.username!r}>"
