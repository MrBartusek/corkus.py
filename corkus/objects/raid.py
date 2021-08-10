from __future__ import annotations
from .base import CorkusBase

class Raid(CorkusBase):
    @property
    def name(self) -> str:
        """Name of the raid"""
        return self._attributes.get("name", "")

    @property
    def completed(self) -> int:
        """Total runs by the player"""
        return self._attributes.get("completed", 0)

    def __repr__(self) -> str:
        return f"<Raid name={self.name!r} completed={self.completed}>"
