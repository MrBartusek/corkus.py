from typing import List

from .base import CorkusBase
from .partial_player import PartialPlayer
from .partial_guild import PartialGuild

class SearchResult(CorkusBase):
    @property
    def players(self) -> List[PartialPlayer]:
        """List of found players"""
        return [PartialPlayer(self.corkus, username = p) for p in self.attributes.get("players", [])]

    @property
    def guilds(self) -> List[PartialGuild]:
        """List of found guilds"""
        return [PartialGuild(self.corkus, g) for g in self.attributes.get("guilds", [])]

    @property
    def term(self) -> str:
        """Search term used to display these results"""
        return self.attributes.get("search", "")

    def __repr__(self) -> str:
        return f"<SearchResult players={self.players} guild={self.guilds}>"
