from __future__ import annotations
from .base import CorkusBase

class TerritoryLocation(CorkusBase):
    """The start and end coordinates of the :py:class:`Territory` area."""
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
        return f"<TerritoryLocation start_x={self.start_x} start_y={self.start_y} end_x={self.end_x} end_y={self.end_y}>"
