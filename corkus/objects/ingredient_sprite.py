from __future__ import annotations
from .base import CorkusBase

class IngredientSprite(CorkusBase):
    @property
    def id(self) -> int:
        """Minecraft item ID that represents this ingredient"""
        return self._attributes.get("id", 0)

    @property
    def damage(self) -> int:
        """I don't have idea what this property does :)"""
        return self._attributes.get("damage", 0)

    def __repr__(self) -> str:
        return f"<IngredientSprite id={self.id} damage={self.damage}>"
