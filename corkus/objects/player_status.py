from __future__ import annotations
from .base import CorkusBase

class PlayerStatus(CorkusBase):
    @property
    def online(self) -> bool:
        return self.attributes.get("online", False)

    @property
    def server(self):
        raise NotImplementedError

    def __repr__(self) -> str:
        return f"<PlayerStatus online={self.online}>"
