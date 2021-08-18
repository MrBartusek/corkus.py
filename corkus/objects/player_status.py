from __future__ import annotations
from typing import Union
from .base import CorkusBase
from .partial_server import PartialServer

class PlayerStatus(CorkusBase):
    """Represents online status of :py:class:`Player`."""
    @property
    def online(self) -> bool:
        """Is player online right now."""
        return self._attributes.get("online", False)

    @property
    def server(self) -> Union[PartialServer, None]:
        """The server that this player is currently on, ``None`` if player is offline."""
        if self._attributes.get("server") is not None:
            return PartialServer(self._corkus, self._attributes.get("server", ""))
        else:
            return None

    def __repr__(self) -> str:
        return f"<PlayerStatus online={self.online}>"
