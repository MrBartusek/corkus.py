from __future__ import annotations
from typing import List

from .base import CorkusBase
from .server import Server
from .partial_online_player import PartialOnlinePlayer

class OnlinePlayers(CorkusBase):
    """List all running servers and players that are online on them."""
    @property
    def servers(self) -> List[Server]:
        """List all running servers."""
        return [Server(self._corkus, name, players) for name, players in self._attributes.items()]

    @property
    def players(self) -> List[PartialOnlinePlayer]:
        """List all online players."""
        return [p for s in self.servers for p in s.players]

    def __repr__(self) -> str:
        return f"<OnlinePlayers servers={len(self.servers)} players={len(self.players)}>"
