from .base import CorkusBase
from .member import Member
from typing import List

class Guild(CorkusBase):
    @property
    def name(self) -> str:
        return self.attributes.get("name", "")

    @property
    def tag(self) -> str:
        return self.attributes.get("prefix", "")

    @property
    def members(self) -> List[Member]:
        return [Member(self.corkus, m) for m in self.attributes.get("members", [])]

    @property
    def level(self) -> int:
        return self.attributes.get("level", 1)

    @property
    def level_progress(self) -> float:
        return self.attributes.get("xp", 0)

    @property
    def territories(self) -> None:
        raise NotImplementedError

    @property
    def banner(self) -> None:
        raise NotImplementedError

    def __repr__(self) -> str:
        return f"<Guild tag={self.tag!r} name={self.name!r}>"
