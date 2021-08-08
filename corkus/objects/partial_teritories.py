from __future__ import annotations
from corkus.objects.teritory import Teritory
from typing import Any, List, TYPE_CHECKING, Coroutine
from .partial_base import PartialBase

if TYPE_CHECKING:
    from corkus import Corkus
    from .guild import Guild

class PartialTeritories(PartialBase):
    """This partial object is returned as a teritories of guild.
    API returns only numbers of teritories owned by a specific guild.
    You can use it to request :py:func:`TerritoryEndpoint.list_all`
    and get detailed list of guilds"""

    def __init__(self, corkus: Corkus, guild: Guild, count: int):
        super().__init__(corkus)
        self._count = count
        self._guild = guild

    @property
    def count(self):
        """Total count of teritories owned by this guild"""
        return self._count

    def __len__(self) -> int:
        return self.count

    async def fetch(self) -> Coroutine[Any, Any, List[Teritory]]:
        """Fetch full server information from API. Returns `None` if server no longer exist"""
        teritories = await self.corkus.territory.list_all()
        return [t for t in teritories if t.guild.name == self._guild.name]
