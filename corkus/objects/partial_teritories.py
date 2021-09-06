from __future__ import annotations
from .territory import Territory
from typing import TYPE_CHECKING, Optional, List
from .partial_base import PartialBase

if TYPE_CHECKING:
    from corkus import Corkus
    from .guild import Guild

class PartialTeritories(PartialBase):
    """This ``Partial`` object is returned as a teritories of :py:class:`Guild`.
    API returns only numbers of teritories owned by a specific guild.
    You can use :py:func:`fetch` function which calls :py:func:`TerritoryEndpoint.list_all() <corkus.endpoints.TerritoryEndpoint.list_all>`
    and return detailed list of teritories owned by this guild."""

    def __init__(self, corkus: Corkus, guild: Guild, count: int):
        super().__init__(corkus)
        self._count = count
        self._guild = guild

    @property
    def count(self) -> int:
        """Total count of teritories owned by this guild."""
        return self._count

    def __len__(self) -> int:
        return self.count

    async def fetch(self, timeout: Optional[int] = None) -> List[Territory]:
        """Fetch full Territory information from API.

        .. include:: ../note_api_call.rst

        :param timeout: Optionally override default timeout.
        """
        teritories = await self._corkus.territory.list_all(timeout)
        return [t for t in teritories if t.guild.name == self._guild.name]
