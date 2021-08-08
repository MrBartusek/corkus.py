from __future__ import annotations
from typing import Literal, Union

from .base import CorkusBase
from .level_range import LevelRange
from .enums import ItemType, Profession
from .material import Material
from .identification import Identification

class Recipe(CorkusBase):
    @property
    def level(self) -> LevelRange:
        """Level range that this item should be used in"""
        return LevelRange(self._corkus, attributes = self._attributes)

    @property
    def id(self) -> str:
        """Return the id of recipe like `Food-13-15` or `Wand-63-65`"""
        return self._attributes.get("id", "")

    @property
    def type(self) -> ItemType:
        """Type of the item"""
        return ItemType(self._attributes.get("type", ItemType.WAND))

    @property
    def skill(self) -> Profession:
        """Skill required to craft this item"""
        return Profession(self._attributes.get("skill", Profession.WOODWORKING))

    @property
    def materials(self) -> Material:
        """Skill required to craft this item"""
        return [Material(self._corkus, m) for m in self._attributes.get("materials", [])]

    @property
    def health_or_damage(self) -> Identification:
        """If this item is a weapon this returns damage dealt by this item, if not, health bonus"""
        return Identification(self._corkus, attributes = self._attributes.get("healthOrDamage", {}))

    @property
    def duration(self) -> Union[None, int]:
        """If item is comsumbale returns how long it will work after use"""
        if "duration" in self._attributes:
            return Identification(self._corkus, attributes = self._attributes.get("duration", {}))
        else:
            return None

    @property
    def charges(self) -> Union[None, Literal[1, 2, 3]]:
        """If item is comsumbale returns how many times it can be used"""
        if self.type in (ItemType.POTION, ItemType.SCROLL, ItemType.FOOD):
            if self.level > 70:
                return 3
            elif self.level > 30:
                return 2
            else:
                return 1
        else:
            return None

    @property
    def durability(self) -> Union[None, Identification]:
        """If item is armour accessory or weapon, return it's durability"""
        if "durability" in self._attributes:
            return Identification(self._corkus, attributes = self._attributes.get("durability", {}))
        else:
            return None

    def __repr__(self) -> str:
        return f"<Recipe level={self.level} type={self.type!r}>"
