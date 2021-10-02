from __future__ import annotations
from typing import List

from .partial_online_player import PartialOnlinePlayer
from .base_server import BaseServer


class Server(BaseServer):
    """Represents a singular Wynncraft Server."""
    @property
    def players(self) -> List[PartialOnlinePlayer]:
        """List of all online players on this server."""
        return [PartialOnlinePlayer(self._corkus, self, username = p) for p in self._attributes]

    @property
    def total_players(self) -> int:
        """Total number of online player on this server."""
        return len(self.players)

    def __repr__(self) -> str:
        return f"<Server name={self.name!r} total_players={self.total_players} players={self.players}>"
