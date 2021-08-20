from __future__ import annotations
from typing import List, Literal, Union

from .base import CorkusBase
from .level_range import LevelRange
from .enums import ItemType, ProfessionType, ItemCategory
from .material import Material
from .identification_values import IdentificationValues

class Recipe(CorkusBase):
    """Needed materials and professions for `Crafting <https://wynncraft.fandom.com/wiki/Crafting>`_ a item with given properties."""
    @property
    def level(self) -> LevelRange:
        """Level range that this item should be used in."""
        return LevelRange(self._corkus, attributes = self._attributes.get("level", {}))

    @property
    def id(self) -> str:
        """Return the id of recipe like ``Food-13-15`` or ``Wand-63-65``."""
        return self._attributes.get("id", "")

    @property
    def type(self) -> ItemType:
        """Type of the item."""
        return ItemType(self._attributes.get("type", ItemType.WAND))

    @property
    def category(self) -> ItemCategory:
        """Category of the item."""
        return ItemCategory.from_type(self.type)

    @property
    def profession(self) -> ProfessionType:
        """Profession required to craft this item."""
        return ProfessionType(self._attributes.get("skill", ProfessionType.WOODWORKING))

    @property
    def materials(self) -> List[Material]:
        """Materials required to craft this item."""
        return [Material(self._corkus, m) for m in self._attributes.get("materials", [])]

    @property
    def health_or_damage(self) -> IdentificationValues:
        """If this item is a weapon this returns damage dealt by this item, if not, health bonus."""
        return IdentificationValues(self._corkus, attributes = self._attributes.get("healthOrDamage", {}))

    @property
    def duration(self) -> Union[None, IdentificationValues]:
        """If item is comsumbale returns how long it will work after use."""
        if "duration" in self._attributes:
            return IdentificationValues(self._corkus, attributes = self._attributes.get("duration", {}))
        else:
            return None

    @property
    def charges(self) -> Union[None, Literal[3]]:
        """If item is comsumbale returns how many times it can be used."""
        if self.type in (ItemType.POTION, ItemType.SCROLL, ItemType.FOOD):
            return 3
        else:
            return None

    @property
    def durability(self) -> Union[None, IdentificationValues]:
        """If item is armour accessory or weapon, return it's durability."""
        if "durability" in self._attributes:
            return IdentificationValues(self._corkus, attributes = self._attributes.get("durability", {}))
        else:
            return None

    def __repr__(self) -> str:
        return f"<Recipe level={self.level} type={self.type!r}>"
