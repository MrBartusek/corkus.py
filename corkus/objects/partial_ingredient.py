from __future__ import annotations
from corkus.objects.base import CorkusBase
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .ingredient import Ingredient

class PartialIngredient(CorkusBase):
    """Represents a ``Partial`` version of :py:class:`Ingredient`."""
    @property
    def name(self) -> str:
        """The name of the ingredient."""
        return self._attributes

    async def fetch(self) -> Ingredient:
        """Fetch full ingredient information from API.

        .. include:: ../note_api_call.rst"""
        return await self._corkus.ingredient.get(self.name)

    def __repr__(self) -> str:
        return f"<PartialIngredient name={self.name!r}>"
