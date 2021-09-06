from __future__ import annotations
from typing import TYPE_CHECKING, Optional

from .partial_base import PartialBase

if TYPE_CHECKING:
    from corkus import Corkus

class IdentificationValues(PartialBase):
    """Represents possible values of :py:class:`Identification`. The actual value of identification
    is randomly selected between :py:attr:`min` and :py:attr:`max` when item is identified or crafted.
    """
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

        if self._max < self._min:
            self._min, self._max = self._max, self._min

    @property
    def min(self) -> int:
        """The lowest possible identification of this property."""
        return self._min

    @property
    def max(self) -> int:
        """The highest possible identification of this property."""
        return self._max

    def __repr__(self) -> str:
        return f"<IdentificationValues min={self.min} max={self.max}>"
