from __future__ import annotations
from typing import TYPE_CHECKING

from corkus.objects.base_partial_member import BasePartialMember

if TYPE_CHECKING:
    from corkus import Corkus
    from .uuid import CorkusUUID
    from .partial_guild import PartialGuild

class LeaderboardPartialMember(BasePartialMember):
    def __init__(self,
        corkus: Corkus,
        uuid: CorkusUUID,
        username: str,
        guild: PartialGuild,
        tag: str
        ):
        super().__init__(corkus, uuid, username, guild)
        self._tag = tag

    @property
    def tag(self) -> str:
        """Three or four letters prefix of guild"""
        return self._tag

    def __repr__(self) -> str:
        return f"<LeaderboardPartialMember username={self._username!r} guild={self._guild}>"
