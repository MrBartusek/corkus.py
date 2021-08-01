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
        return self.attributes.get("name", "")

    @property
    def uuid(self) -> CorkusUUID:
        return CorkusUUID(self.attributes.get("uuid", ""))

    @property
    def contributed_xp(self) -> int:
        return self.attributes.get("contributed", 0)

    @property
    def join_date(self) -> datetime:
        return iso8601.parse_date(self.attributes.get("join", "1970"))

    @property
    def guild(self) -> Guild:
        return self._guild

    async def fetch_player(self) -> Player:
        return await self.corkus.player.get(self.uuid)
