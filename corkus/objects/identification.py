from __future__ import annotations
from typing import TYPE_CHECKING

from .partial_base import PartialBase

if TYPE_CHECKING:
    from corkus import Corkus

class Identification(PartialBase):
    """Identification is a bonnus applied to an item to increse or decrees it's effectiveness.
    The actual value of identification is randomly selected between :py:attr:`minimum` and :py:attr:`maximum`."""
    def __init__(self, corkus: Corkus, *, attributes: dict = None):
        super().__init__(corkus)
        self._min = attributes.get("minimum", 0)
        self._max = attributes.get("maximum", 0)

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
