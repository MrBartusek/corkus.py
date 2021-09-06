from __future__ import annotations
from typing import List, TYPE_CHECKING
from enum import Enum
from .base import CorkusBase
from .partial_online_player import PartialOnlinePlayer

if TYPE_CHECKING:
    from corkus import Corkus

class ServerType(Enum):
    """Type of :py:class:`Server`."""
    REGULAR = "WC"
    """Regular Wynncraft servers."""

    YOUTUBE = "YT"
    """Servers restricted to players with :py:attr:`PlayerRank.MEDIA` rank."""

class Server(CorkusBase):
    """Represents a singular Wynncraft Server."""
    def __init__(self, corkus: Corkus, name: str, players: List[str]):
        self._name = name
        super().__init__(corkus, players)

    @property
    def name(self) -> str:
        """The name of server like ``WC1`` or ``WC16`` or ``YT``."""
        return self._name

    @property
    def players(self) -> List[PartialOnlinePlayer]:
        """List of all online players on this server."""
        return [PartialOnlinePlayer(self._corkus, self, username = p) for p in self._attributes]

    @property
    def total_players(self) -> int:
        """Total number of online player on this server."""
        return len(self.players)

    @property
    def type(self) -> ServerType:
        """Type of the server, most servers are stanard servers."""
        return ServerType("".join([i for i in self._name if not i.isdigit()]))

    @property
    def regular(self) -> bool:
        """Is this server a regular server (:py:attr:`type` is :py:attr:`ServerType.REGULAR`)."""
        return self.type == ServerType.REGULAR

    def __repr__(self) -> str:
        return f"<Server name={self.name!r} total_players={self.total_players} players={self.players}>"
