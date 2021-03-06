from __future__ import annotations
from typing import TYPE_CHECKING, Optional
from .partial_base import PartialBase

if TYPE_CHECKING:
    from corkus import Corkus

class LevelRange(PartialBase):
    """Range of levels where crafted item is most effective."""

    def __init__(self, corkus: Corkus, *,
        attributes: Optional[dict] = None,
        min: Optional[int] = None,
        max: Optional[int] = None
        ):
        super().__init__(corkus)

        if attributes is None:
            attributes = {}

        self._min = attributes.get("minimum") or min or 0
        self._max = attributes.get("maximum") or max or 0

    @property
    def min(self) -> int:
        """Minimal combat level needed in order for this item to be used."""
        return self._min

    @property
    def max(self) -> int:
        """Recommended maximal combat level for this item."""
        return self._max

    def __repr__(self) -> str:
        return f"<LevelRange min={self.min} max={self.max}>"
