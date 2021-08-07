from __future__ import annotations
from typing import Union
from .base import CorkusBase
from .partial_server import PartialServer

class PlayerStatus(CorkusBase):
    @property
    def online(self) -> bool:
        """Is player online right now"""
        return self._attributes.get("online", False)

    @property
    def server(self) -> Union[PartialServer, None]:
        if self._attributes.get("server") is not None:
            return PartialServer(self._corkus, self._attributes.get("server", ""))
        else:
            return None

    def __repr__(self) -> str:
        return f"<PlayerStatus online={self.online}>"
