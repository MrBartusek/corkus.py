from __future__ import annotations
from typing import List, Union
from corkus.objects.member import Member

from corkus.utils.utils import Utils
from .base import CorkusBase
from .server import Server
from .partial_online_player import PartialOnlinePlayer
from .player import Player
from .partial_player import PartialPlayer

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

    @property
    def regular_players(self) -> List[PartialOnlinePlayer]:
        """List all online players that are playing on regular servers."""
        return [p for s in self.servers if s.regular for p in s.players]

    def get_player_server(self, player: Union[str, Player, PartialPlayer, PartialOnlinePlayer, Member]) -> Union[Server, None]:
        """Get the server that player is currently playing on. Returns ``None`` if player is offline.

        :param player: Player username or player object to check for.
        """
        username = Utils.player_to_username(player)
        for p in self.players:
            if p.username == username:
                return p.server
        return None

    def is_player_online(self, player: Union[str, Player, PartialPlayer, PartialOnlinePlayer, Member]) -> bool:
        """Check if player is online.

        :param player: Player username or player object to check for.
        """
        return self.get_player_server(player) is not None

    def __repr__(self) -> str:
        return f"<OnlinePlayers servers={len(self.servers)} players={len(self.players)}>"
