from __future__ import annotations
from typing import TYPE_CHECKING

from corkus.objects.partial_player import PartialPlayer

if TYPE_CHECKING:
    from corkus import Corkus
    from .guild import Guild
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

    async def fetch_guild(self) -> Guild:
        return await self._guild.fetch()

    async def fetch_member(self) -> Member:
        guild = await self.fetch_guild()
        member = [m for m in guild.members if m.uuid == self._uuid]
        if len(member) == 1:
            return member
        else:
            return None

    def __repr__(self) -> str:
        return f"<PartialMember username={self._username!r} guild={self._guild}>"
