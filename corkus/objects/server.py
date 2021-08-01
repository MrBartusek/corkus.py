from __future__ import annotations
from typing import List, TYPE_CHECKING
from enum import Enum
from .base import CorkusBase
from .partial_player import PartialPlayer

if TYPE_CHECKING:
    from corkus import Corkus

class ServerType(Enum):
    STANDARD = "WC"
    YOUTUBE = "YT"

class Server(CorkusBase):
    def __init__(self, corkus: Corkus, name: str, players: List[str]):
        self._name = name
        super().__init__(corkus, players)

    @property
    def name(self) -> str:
        """The name of server"""
        return self._name

    @property
    def players(self) -> List[PartialPlayer]:
        """List of all online players on this server"""
        return [PartialPlayer(self.corkus, username = p) for p in self.attributes]

    @property
    def total_players(self) -> int:
        """Total number of online player on this server"""
        return len(self.players)

    @property
    def type(self) -> ServerType:
        """Type of the server, most servers are stanard servers"""
        return ServerType("".join([i for i in self._name if not i.isdigit()]))

    def __repr__(self) -> str:
        return f"<Server name={self.name!r} total_players={self.total_players} players={self.players}>"
