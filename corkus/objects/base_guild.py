from __future__ import annotations
from .base import CorkusBase
from .partial_teritories import PartialTeritories
from datetime import datetime
from iso8601 import iso8601

class BaseGuild(CorkusBase):
    @property
    def name(self) -> str:
        """The name of the guild"""
        return self._attributes.get("name", "")

    @property
    def tag(self) -> str:
        """Three or four letters prefix of guild"""
        return self._attributes.get("prefix", "")

    @property
    def created(self) -> datetime:
        return iso8601.parse_date(self._attributes.get("created", "1970"))

    @property
    def level(self) -> int:
        """Level of the guild 1-100"""
        return self._attributes.get("level", 1)

    @property
    def territories(self) -> PartialTeritories:
        """Teritories owned by the guild"""
        return PartialTeritories(
            corkus = self._corkus,
            guild = self,
            count = self._attributes.get("territories", 0)
        )

    @property
    def banner(self) -> None:
        """Guild banner"""
        raise NotImplementedError

    def __repr__(self) -> str:
        return f"<BaseGuild tag={self.tag!r} name={self.name!r}>"
