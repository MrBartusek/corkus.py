from enum import Enum
import iso8601
from datetime import datetime
from .base import CorkusBase
from .uuid import CorkusUUID

class GuildRank(Enum):
    OWNER = "OWNER"
    CHIEF = "CHIEF"
    CAPTAIN = "CAPTAIN"
    RECRUITER = "RECRUITER"
    RECRUIT = "RECRUIT"

class Member(CorkusBase):
    @property
    def username(self) -> int:
        return self.attributes.get("username", "")

    @property
    def uuid(self) -> CorkusUUID:
        return CorkusUUID(self.attributes.get("uuid", ""))

    @property
    def contributed_xp(self) -> int:
        return self.attributes.get("contributed", 0)

    @property
    def join_date(self) -> datetime:
        return iso8601.parse_date(self.attributes.get("join", "1970-01-01T00:00:00.000Z"))
