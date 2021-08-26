from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Literal

from .partial_player import PartialPlayer

if TYPE_CHECKING:
    from corkus import Corkus
    from .uuid import CorkusUUID
    from .server import Server


class PartialOnlinePlayer(PartialPlayer):
    """Represents a :py:class:`PartialPlayer` that is currently online."""
    def __init__(self, corkus: Corkus, server: Server, *, uuid: Optional[CorkusUUID] = None, username: Optional[str] = None):
        super().__init__(corkus, uuid = uuid, username = username)
        self._server = server

    @property
    def online(self) -> Literal[True]:
        """Is player online right now, always ``True`` obviously."""
        return True

    @property
    def server(self) -> Server:
        """The server that this player is currently on."""
        return self._server

    def __repr__(self) -> str:
        return super().__repr__().replace("PartialPlayer", f"PartialOnlinePlayer server={self._server.name!r} ")
