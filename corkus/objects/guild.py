from __future__ import annotations
from .member import Member
from typing import List
from .base_guild import BaseGuild

class Guild(BaseGuild):
    @property
    def members(self) -> List[Member]:
        """List of all guild members"""
        return [Member(self._corkus, self , m) for m in self._attributes.get("members", [])]

    @property
    def level_progress(self) -> float:
        """Progress to next level in precentage 1-100%"""
        return self._attributes.get("xp", 0)

    def __repr__(self) -> str:
        return f"<Guild tag={self.tag!r} name={self.name!r}>"
