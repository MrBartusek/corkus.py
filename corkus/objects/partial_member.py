from __future__ import annotations
from typing import TYPE_CHECKING

from corkus.objects.base_partial_member import BasePartialMember

if TYPE_CHECKING:
    from corkus import Corkus
    from .uuid import CorkusUUID
    from .member import GuildRank
    from .partial_guild import PartialGuild

class PartialMember(BasePartialMember):
    """Represents a ``Partial`` version of :py:class:`Member`."""
    def __init__(self,
        corkus: Corkus,
        uuid: CorkusUUID,
        username: str,
        guild: PartialGuild,
        rank: GuildRank
        ):
        super().__init__(corkus, uuid, username, guild)
        self._rank = rank

    @property
    def rank(self) -> GuildRank:
        """Player's rank in guild."""
        return self._rank

    def __repr__(self) -> str:
        return f"<PartialMember username={self._username!r} guild={self._guild}>"
