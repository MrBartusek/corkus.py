from __future__ import annotations
from .base import CorkusBase

class IngredientSprite(CorkusBase):
    """Represents visual look of :py:class:`Ingredient`"""
    @property
    def id(self) -> int:
        """Minecraft item ID that represents this ingredient."""
        return self._attributes.get("id", 0)

    @property
    def damage(self) -> int:
        """I honestly don't have idea what this property does, if you know
        please `create a issue <https://github.com/MrBartusek/corkus.py/issues/new/choose>`_"""
        return self._attributes.get("damage", 0)

    def __repr__(self) -> str:
        return f"<IngredientSprite id={self.id} damage={self.damage}>"
