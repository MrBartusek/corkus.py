from corkus.objects.playtime import PlayerPlaytime
from enum import Enum
from typing import Union
import iso8601
from datetime import datetime

from .base import CorkusBase
from .uuid import CorkusUUID
from .partial_member import PartialMember
from .partial_guild import PartialGuild
from .member import GuildRank
from .player_status import PlayerStatus
from .player_statistics import PlayerStatistics
from .player_class import PlayerClass

class PlayerRank(Enum):
    ADMINISTRATOR = "Administrator"
    MODERATOR = "Moderator"
    BUILDER = "Builder"
    ITEM = "Item"
    GAME_MASTER = "Game Master"
    CMD = "CMD"
    MUSIC = "Music"
    HYBRID = "Hybrid"
    MEDIA = "Media"
    PLAYER = "Player"

class PlayerTag(Enum):
    PLAYER = "PLAYER"
    VIP = "VIP"
    VIP_PLUS = "VIP+"
    HERO = "HERO"
    CHAMPION = "CHAMPION"

class Player(CorkusBase):
    @property
    def username(self) -> str:
        """Minecraft username of player"""
        return self.attributes.get("username", "")

    @property
    def uuid(self) -> CorkusUUID:
        """Minecraft UUID of player"""
        return CorkusUUID(self.attributes.get("uuid", ""))

    @property
    def rank(self) -> PlayerRank:
        """Player Wynncraft Team Rank, if not in content team defaults to PLAYER"""
        return PlayerRank(self.attributes.get("rank", PlayerRank.PLAYER))

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
    def tag(self):
        """Player's rank bought from Wynncraft Store"""
        return PlayerTag(self.attributes.get("meta", {}).get("tag", {}).get("value", PlayerTag.PLAYER))

    @property
    def veteran(self):
        "Is player a veteran eg. had VIP before August 1, 2014 which was when the 1.12 update was released and Minecraft EULA changed"
        return self.attributes.get("meta", {}).get("veteran", False)

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
