from __future__ import annotations
from typing import TYPE_CHECKING, Optional

from corkus.objects.partial_player import PartialPlayer

if TYPE_CHECKING:
    from corkus import Corkus
    from .uuid import CorkusUUID
    from .member import Member
    from .partial_guild import PartialGuild

class BasePartialMember(PartialPlayer):
    def __init__(self,
        corkus: Corkus ,
        uuid: CorkusUUID,
        username: str,
        guild: PartialGuild
    ):
        super().__init__(corkus, uuid=uuid, username=username)
        self._guild = guild

    @property
    def player(self) -> PartialPlayer:
        """Reduce to to :class:`PartialPlayer`. Usefull when you want
        to fetch player information not member information.
        """
        return super()

    @property
    def guild(self) -> PartialGuild:
        """The guild that this member is a part of."""
        return self._guild

    async def fetch(self, timeout: Optional[int] = None) -> Member:
        """Fetch more guild data about this member from API.

        .. include:: ../note_api_call.rst

        :param timeout: Optionally override default timeout.
        """
        guild = await self._guild.fetch(timeout)
        return next((m for m in guild.members if m.uuid == self._uuid), None)

    def __repr__(self) -> str:
        return f"<BasePartialMember username={self._username!r} guild={self._guild}>"
