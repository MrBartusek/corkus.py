from __future__ import annotations
from typing import TYPE_CHECKING

from corkus.objects.base_partial_member import BasePartialMember

if TYPE_CHECKING:
    from corkus import Corkus
    from .uuid import CorkusUUID
    from .partial_guild import PartialGuild

class LeaderboardPartialMember(BasePartialMember):
    """Diffrent version of :py:class:`PartialMember` returned by :py:class:`LeaderboardEndpoint <corkus.endpoints.LeaderboardEndpoint>`."""
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
        """Prefix displayed as a shorter 3 or 4 letters representation of guild.
        Like ``AVO``, ``ERN`` or ``YIN``. It's mostly upper-case but it's not a requirement.
        It's unique across all guild."""
        return self._tag

    def __repr__(self) -> str:
        return f"<LeaderboardPartialMember username={self._username!r} guild={self._guild}>"
