from __future__ import annotations
from corkus.objects.guild import Guild
from typing import TYPE_CHECKING

from corkus.objects.partial_player import PartialPlayer

if TYPE_CHECKING:
    from corkus import Corkus
    from .uuid import CorkusUUID
    from .member import Member, GuildRank
    from .partial_guild import PartialGuild

class PartialMember(PartialPlayer):
    def __init__(self,
        corkus: Corkus ,
        uuid: CorkusUUID,
        username: str,
        guild: PartialGuild,
        rank: GuildRank
    ):
        super().__init__(corkus, uuid=uuid, username=username)
        self._guild = guild
        self._rank = rank

    @property
    def player(self) -> PartialPlayer:
        return super()

    @property
    def guild(self) -> Guild:
        return self.guild

    async def fetch(self) -> Member:
        guild = await self._guild.fetch()
        member = [m for m in guild.members if m.uuid == self._uuid]
        if len(member) == 1:
            return member
        else:
            return None

    def __repr__(self) -> str:
        return f"<PartialMember username={self._username!r} guild={self._guild}>"
