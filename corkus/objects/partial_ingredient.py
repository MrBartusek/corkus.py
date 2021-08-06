from __future__ import annotations
from corkus.objects.base import CorkusBase
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .ingredient import Ingredient

class PartialIngredient(CorkusBase):
    @property
    def name(self) -> str:
        """The name of the ingredient"""
        return self.attributes

    async def fetch(self) -> Ingredient:
        """Fetch full ingredient information from API"""
        return await self.corkus.ingredient.get(self.name)

    def __repr__(self) -> str:
        return f"<PartialIngredient name={self.name!r}>"
