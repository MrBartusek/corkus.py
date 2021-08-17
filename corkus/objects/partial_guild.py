from __future__ import annotations
from corkus.objects.base import CorkusBase
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .guild import Guild

class PartialGuild(CorkusBase):
    @property
    def name(self) -> str:
        """The name of the guild."""
        return self._attributes

    async def fetch(self, timeout: Optional[int] = None) -> Guild:
        """Fetch full guild information from API.

        .. include:: ../note_api_call.rst

        :param timeout: Optionally override default timeout.
        """
        return await self._corkus.guild.get(self.name, timeout)

    def __repr__(self) -> str:
        return f"<PartialGuild name={self.name!r}>"
