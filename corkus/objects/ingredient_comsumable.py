from __future__ import annotations
from .base import CorkusBase

class IngredientComsumableModifiers(CorkusBase):
    @property
    def duration(self) -> int:
        """Modifier on item duration"""
        return self._attributes.get("duration", 0)

    @property
    def charges(self) -> int:
        """Modifier on item charges"""
        return self._attributes.get("charges", 0)

    def __repr__(self) -> str:
        return f"<IngredientComsumableModifiers duration={self.duration} charges={self.charges}>"
