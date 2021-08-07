from __future__ import annotations
from .base import CorkusBase

class TeritoryLocation(CorkusBase):
    """The start and end coordinates of the territory's area"""
    @property
    def start_x(self) -> int:
        return self._attributes.get("startX", 0)

    @property
    def start_y(self) -> int:
        return self._attributes.get("startY", 0)

    @property
    def end_x(self) -> int:
        return self._attributes.get("endX", 0)

    @property
    def end_y(self) -> int:
        return self._attributes.get("endY", 0)

    def __repr__(self) -> str:
        return f"<TeritoryLocation start_x={self.start_x} start_y={self.start_y} end_x={self.end_x} end_y={self.end_y}>"
