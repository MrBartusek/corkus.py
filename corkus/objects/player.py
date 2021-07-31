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

class PlayerRank(Enum):
    """Player Wynncraft Team Rank, if not in content team defaults to PLAYER"""

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

class Player(CorkusBase):
    @property
    def username(self) -> str:
        return self.attributes.get("username", "")

    @property
    def uuid(self) -> CorkusUUID:
        return CorkusUUID(self.attributes.get("uuid", ""))

    @property
    def rank(self) -> PlayerRank:
        return PlayerRank(self.attributes.get("rank", PlayerRank.PLAYER))

    @property
    def in_content_team(self) -> bool:
        return self.rank != PlayerRank.PLAYER

    @property
    def join_date(self) -> datetime:
        return iso8601.parse_date(self.attributes.get("meta", {}).get("firstJoin", "1970"))

    def last_online(self) -> datetime:
        return iso8601.parse_date(self.attributes.get("meta", {}).get("lastJoin", "1970"))

    @property
    def status(self) -> PlayerStatus:
        return PlayerStatus(self.corkus, self.attributes.get("meta", {}).get("location", {}))

    @property
    def playtime(self):
        raise NotImplementedError

    @property
    def tag(self):
        raise NotImplementedError

    @property
    def veteran(self):
        return self.attributes.get("meta", {}).get("veteran", False)

    @property
    def classes(self):
        raise NotImplementedError

    @property
    def member(self) -> Union[PartialMember, None]:
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
        if self.attributes.get("guild", {}).get("name", None) is None:
            return None
        else:
            return PartialGuild(
                corkus = self.corkus,
                name = self.attributes.get("guild", {}).get("name", "")
            )

    @property
    def stats(self):
        raise NotImplementedError

    @property
    def ranking(self):
        raise NotImplementedError

    def __repr__(self) -> str:
        return f"<Player username={self.username!r}>"
