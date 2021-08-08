from __future__ import annotations
from typing import TYPE_CHECKING, Optional
from .partial_base import PartialBase

if TYPE_CHECKING:
    from corkus import Corkus

class LevelRange(PartialBase):
    """Range of levels where crafted item is most effective"""

    def __init__(self, corkus: Corkus, *,
        attributes: Optional[dict] = None,
        minimum: Optional[int] = None,
        maximum: Optional[int] = None
        ):
        super().__init__(corkus)

        if attributes is None:
            attributes = {}

        self._min = attributes.get("minimum") or minimum or 0
        self._max = attributes.get("maximum") or maximum or 0

    @property
    def minimum(self) -> int:
        """The lowest possible identification of this property"""
        return self._min

    @property
    def maximum(self) -> int:
        """The highest possible identification of this property"""
        return self._max

    def __repr__(self) -> str:
        return f"<Identification min={self.minimum} max={self.maximum}>"
