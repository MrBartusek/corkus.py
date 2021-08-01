from __future__ import annotations
from typing import TYPE_CHECKING

from .partial_base import PartialBase

if TYPE_CHECKING:
    from corkus import Corkus
    from .guild import Guild

class PartialGuild(PartialBase):
    def __init__(self, corkus: Corkus, name: str):
        super().__init__(corkus)
        self._name = name

    @property
    def name(self) -> str:
        """The name of the guild"""
        return self._name

    async def fetch(self) -> Guild:
        """Fetch full guild information from API"""
        return await self.corkus.guild.get(self._name)

    def __repr__(self) -> str:
        return f"<PartialGuild name={self._name!r}>"
