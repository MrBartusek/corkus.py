from __future__ import annotations
from corkus.objects.base import CorkusBase
from typing import TYPE_CHECKING, Any, Coroutine

if TYPE_CHECKING:
    from .guild import Guild

class PartialGuild(CorkusBase):
    @property
    def name(self) -> str:
        """The name of the guild"""
        return self._attributes

    async def fetch(self) -> Coroutine[Any, Any, Guild]:
        """Fetch full guild information from API"""
        return await self._corkus.guild.get(self.name)

    def __repr__(self) -> str:
        return f"<PartialGuild name={self.name!r}>"
