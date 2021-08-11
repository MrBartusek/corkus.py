from __future__ import annotations
from typing import List

from .base import CorkusBase
from .partial_player import PartialPlayer
from .partial_guild import PartialGuild

class SearchResult(CorkusBase):
    """Combined result of search for :py:class:`Player` and :py:class:`Guild`."""
    @property
    def players(self) -> List[PartialPlayer]:
        """List of found players."""
        return [PartialPlayer(self._corkus, username = p) for p in self._attributes.get("players", [])]

    @property
    def guilds(self) -> List[PartialGuild]:
        """List of found guilds."""
        return [PartialGuild(self._corkus, g) for g in self._attributes.get("guilds", [])]

    @property
    def term(self) -> str:
        """Search term used to display these results."""
        return self._attributes.get("search", "")

    def __repr__(self) -> str:
        return f"<SearchResult players={self.players} guild={self.guilds}>"
