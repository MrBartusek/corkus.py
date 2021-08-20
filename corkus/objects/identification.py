from __future__ import annotations
from typing import TYPE_CHECKING, Optional

from .partial_base import PartialBase

if TYPE_CHECKING:
    from corkus import Corkus
    from .identification_values import IdentificationValues
    from .identification_type import IdentificationType

class Identification(PartialBase):
    """Identification is a bonnus applied to an item to increse or decreese it's effectiveness."""
    def __init__(self, corkus: Corkus, type: IdentificationType, *, value: Optional[int] = None, values: Optional[IdentificationValues] = None):
        super().__init__(corkus)
        self._type = type
        self._value = value
        self._values = values

    @property
    def type(self) -> IdentificationType:
        """Type of the identification."""
        return self._type

    @property
    def value(self) -> int:
        """If this identification is returned from pre-identified item thus returns
        actually value on the item. In other cases return ``None``."""
        return self._value

    @property
    def values(self) -> IdentificationValues:
        """If this identification is in fact rolled and not static return
        it's possible values."""
        return self._values

    def __repr__(self) -> str:
        result = "<Identification"
        if self.value is not None:
            result += f" value={self.value}"
        if self.values is not None:
            result += f" values={self.values}"
        return result + ">"
