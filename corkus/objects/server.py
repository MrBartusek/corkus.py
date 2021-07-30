from typing import List
from enum import Enum
from .base import CorkusBase
from .partial_player import PartialPlayer

class ServerType(Enum):
    """ Type of the server, most servers are stanard servers"""

    STANDARD = "WC"
    YT = "YT"

class Server(CorkusBase):
    def __init__(self, corkus, name: str, players: List[str]):
        self._name = name
        super().__init__(corkus, players)

    @property
    def name(self) -> str:
        return self._name

    @property
    def players(self) -> List[PartialPlayer]:
        return [PartialPlayer(self.corkus, username = p) for p in self.attributes]

    @property
    def total_players(self) -> int:
        return len(self.players)

    @property
    def type(self) -> ServerType:
        return ServerType("".join([i for i in self._name if not i.isdigit()]))
