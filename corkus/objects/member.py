from __future__ import annotations
from typing import TYPE_CHECKING
from enum import Enum
import iso8601
from datetime import datetime

from .base import CorkusBase
from .uuid import CorkusUUID

if TYPE_CHECKING:
    from .guild import Guild
    from corkus import Corkus
    from .player import Player

class GuildRank(Enum):
    OWNER = "OWNER"
    CHIEF = "CHIEF"
    CAPTAIN = "CAPTAIN"
    RECRUITER = "RECRUITER"
    RECRUIT = "RECRUIT"

class Member(CorkusBase):
    def __init__(self, corkus: Corkus, guild: Guild, attributes: dict):
        self._guild = guild
        super().__init__(corkus, attributes)

    @property
    def username(self) -> int:
        """Minecraft username of player"""
        return self.attributes.get("name", "")

    @property
    def uuid(self) -> CorkusUUID:
        """Minecraft UUID of player"""
        return CorkusUUID(self.attributes.get("uuid", ""))

    @property
    def contributed_xp(self) -> int:
        """Total number of contributed experience by this player"""
        return self.attributes.get("contributed", 0)

    @property
    def join_date(self) -> datetime:
        """Date and time when player joined the guild"""
        return iso8601.parse_date(self.attributes.get("join", "1970"))

    @property
    def guild(self) -> Guild:
        """The guild that this member is a part of"""
        return self._guild

    async def fetch_player(self) -> Player:
        """Fetch player data of this member from API"""
        return await self.corkus.player.get(self.uuid)
