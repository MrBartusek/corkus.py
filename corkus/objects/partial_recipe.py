from __future__ import annotations
from typing import TYPE_CHECKING, Optional

from .base import CorkusBase
from .enums import ItemType
from .level_range import LevelRange

if TYPE_CHECKING:
    from .recipe import Recipe

class PartialRecipe(CorkusBase):
    """Represents a ``Partial`` version of :py:class:`Recipe`."""
    @property
    def id(self) -> str:
        """Return the id of recipe like ``Food-13-15`` or ``Wand-63-65``."""
        return self._attributes

    @property
    def type(self) -> ItemType:
        """Type of the item."""
        return ItemType(self.id.split("-")[0].upper())

    @property
    def level(self) -> LevelRange:
        """Level range that this item should be used in."""
        return LevelRange(self._corkus,
            min = int(self.id.split("-")[1].upper()),
            max = int(self.id.split("-")[2].upper())
        )

    async def fetch(self, timeout: Optional[int] = None) -> Recipe:
        """Fetch full recipe information from API.

        .. include:: ../note_api_call.rst

        :param timeout: Optionally override default timeout.
        """
        return await self._corkus.recipe.get_by_id(self.id, timeout)

    def __repr__(self) -> str:
        return f"<PartialRecipe id={self.id!r}>"
