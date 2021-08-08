from __future__ import annotations
from typing import TYPE_CHECKING, Any, Coroutine

from .base import CorkusBase
from .enums import ItemType
from .level_range import LevelRange

if TYPE_CHECKING:
    from .recipe import Recipe

class PartialRecipe(CorkusBase):
    @property
    def id(self) -> str:
        """Return the id of recipe like `Food-13-15` or `Wand-63-65`"""
        return self._attributes

    @property
    def type(self) -> ItemType:
        """Type of the item"""
        return ItemType(self.id.split("-")[0].upper())

    @property
    def level(self) -> LevelRange:
        """Level range that this item should be used in"""
        return LevelRange(self._corkus,
            minimum = int(self.id.split("-")[1].upper()),
            maximum = int(self.id.split("-")[2].upper())
        )

    async def fetch(self) -> Coroutine[Any, Any, Recipe]:
        """Fetch full guild information from API"""
        return await self._corkus.recipe.get_by_id(self.id)

    def __repr__(self) -> str:
        return f"<PartialRecipe id={self.id!r}>"
