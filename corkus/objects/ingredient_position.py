from __future__ import annotations
from .base import CorkusBase

class IngredientPositionModifiers(CorkusBase):
    """Modifier of :py:class:`Ingredient` that change effectiveness of other ingredients in the grid."""
    @property
    def right(self) -> int:
        """Ingredient effectiveness modifier in precentage to ingredients to the right of this one."""
        return self._attributes.get("right", 0)

    @property
    def left(self) -> int:
        """Ingredient effectiveness modifier in precentage to ingredients to the left of this one."""
        return self._attributes.get("left", 0)

    @property
    def above(self) -> int:
        """Ingredient effectiveness modifier in precentage to ingredients above of this one."""
        return self._attributes.get("above", 0)

    @property
    def under(self) -> int:
        """Ingredient effectiveness modifier in precentage to ingredients under this one."""
        return self._attributes.get("under", 0)

    @property
    def touching(self) -> int:
        """Ingredient effectiveness modifier in precentage to ingredients touching this one."""
        return self._attributes.get("touching", 0)

    @property
    def not_touching(self) -> int:
        """Ingredient effectiveness modifier in precentage to ingredients not touching this one."""
        return self._attributes.get("notTouching", 0)
