from .base import CorkusBase
from .member import Member
from typing import List
from datetime import datetime
from iso8601 import iso8601

class BaseGuild(CorkusBase):
    @property
    def name(self) -> str:
        """The name of the guild"""
        return self.attributes.get("name", "")

    @property
    def tag(self) -> str:
        """Three or four letters prefix of guild"""
        return self.attributes.get("prefix", "")

    @property
    def created(self) -> datetime:
        return iso8601.parse_date(self.attributes.get("created", "1970"))

    @property
    def level(self) -> int:
        """Level of the guild 1-100"""
        return self.attributes.get("level", 1)

    @property
    def territories(self) -> None:
        """Teritories owned by the guild"""
        raise NotImplementedError

    @property
    def banner(self) -> None:
        """Guild banner"""
        raise NotImplementedError

    def __repr__(self) -> str:
        return f"<BaseGuild tag={self.tag!r} name={self.name!r}>"
