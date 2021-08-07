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

class BasePlayer(CorkusBase):
    @property
    def uuid(self) -> CorkusUUID:
        """Minecraft UUID of player"""
        return CorkusUUID(self.attributes.get("uuid", ""))

    @property
    def rank(self) -> PlayerRank:
        """Player Wynncraft Team Rank, if not in content team defaults to PLAYER"""
        return PlayerRank(self.attributes.get("rank", PlayerRank.PLAYER))

    @property
    def tag(self):
        """Player's rank bought from Wynncraft Store"""
        return PlayerTag(self.attributes.get("meta", {}).get("tag", {}).get("value", PlayerTag.PLAYER))

    @property
    def veteran(self):
        "Is player a veteran eg. had VIP before August 1, 2014 which was when the 1.12 update was released and Minecraft EULA changed"
        return self.attributes.get("meta", {}).get("veteran", False)

    def __repr__(self) -> str:
        return f"<BasePlayer uuid={self.uuid!r}>"