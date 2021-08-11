from __future__ import annotations
from typing import Literal, List

from .base import CorkusBase
from .enums import ProfessionType
from .ingredient_sprite import IngredientSprite
from .ingredient_position import IngredientPositionModifiers
from .ingredient_comsumable import IngredientComsumableModifiers
from .ingredient_item import IngredientItemModifiers

class Ingredient(CorkusBase):
    """Crafting Ingredients are items found in the world of
    Wynncraft used to add extra effects onto crafted items."""
    @property
    def name(self) -> str:
        """The name of the ingredient."""
        return self._attributes.get("name", "")

    @property
    def tier(self) -> Literal[0, 1, 2, 3]:
        """Number of stars on the ingredient."""
        return self._attributes.get("tier", 0)

    @property
    def reqired_level(self) -> int:
        """Level that an player must get on all of the :py:attr:`~reqired_professions` in order to use this ingredient."""
        return self._attributes.get("level", 0)

    @property
    def reqired_professions(self) -> List[ProfessionType]:
        """List of professions on which player must get :py:attr:`~reqired_level` in order to use this ingredient."""
        return [ProfessionType(p) for p in self._attributes.get("skills", {})]

    @property
    def sprite(self) -> IngredientSprite:
        """Describes look of ingredient in-game."""
        return IngredientSprite(self._corkus, self._attributes.get("sprite", {}))

    @property
    def identifications(self):
        raise NotImplementedError

    @property
    def position_modifiers(self) -> IngredientPositionModifiers:
        """How this ingredient affect other ones in the grid."""
        return IngredientPositionModifiers(self._corkus, self._attributes.get("ingredientPositionModifiers", {}))

    @property
    def item_modifiers(self) -> IngredientItemModifiers:
        """Additional modifiers applied only on not consumable items like armour, weapons or jewelry."""
        return IngredientItemModifiers(self._corkus, self._attributes.get("itemOnlyIDs", {}))

    @property
    def consumable_modifiers(self) -> IngredientComsumableModifiers:
        """Additional modifiers applied only on comsumable items like food, potions and scrolls."""
        return IngredientComsumableModifiers(self._corkus, self._attributes.get("consumableOnlyIDs", {}))

    def __repr__(self) -> str:
        return f"<Ingredient name={self.name!r}>"
