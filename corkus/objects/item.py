from __future__ import annotations
from typing import Union
from enum import Enum

from .base import CorkusBase
from .enums import ItemType
from .player_class import ClassType
from .color import Color
from .quest import Quest

class ItemTier(Enum):
    """Rarity tier of the item"""

    SET = "SET"
    NORMAL = "NORMAL"
    UNIQUE = "UNIQUE"
    RARE = "RARE"
    LEGENDARY = "LEGENDARY"
    FABLED = "FABLED"
    MYTHIC = "MYTHIC"

class ArmourType(Enum):
    """Material from which armour is made, same as in vanilla."""

    LEATHER = "LEATHER"
    IRON = "IRON"
    CHAIN = "CHAIN"
    GOLDEN = "GOLDEN"
    DIAMOND = "DIAMOND"

class ItemRestrictions(Enum):
    """Restrictions applied to some items."""

    UNTRADABLE = "UNTRADABLE"
    """Items that cannot be traded or dropped."""

    QUEST_ITEM = "QUEST_ITEM"
    """A special kind of :py:attr:`UNTRADABLE` items awarded during
    or after completing a quest."""

class Item(CorkusBase):
    """Represents regular (non-crafted) Wynncraft item."""
    @property
    def name(self) -> str:
        """The name of the item."""
        return self._attributes.get("name", "")

    @property
    def display_name(self) -> str:
        """Name that should be displayed to end-user, usually match :py:attr:`name`.

        .. caution::
                This property may not be reliable. See:
                `Wynncraft/WynncraftAPI19 <https://github.com/Wynncraft/WynncraftAPI/issues/19>`_."""
        return self._attributes.get("displayName", self.name)

    @property
    def type(self) -> ItemType:
        """Type of the item."""
        return ItemType(self._attributes.get("type", self._attributes.get("accessoryType", "Wand")).upper())

    @property
    def tier(self) -> ItemTier:
        """Item rarity tier."""
        return ItemTier(self._attributes.get("tier", "Normal").upper())

    @property
    def set(self) -> Union[str, None]:
        """The name of the set this item is part of. ``None`` if not part of a set.

        .. caution::
                This property is currently bugged and works only for ``Leaf`` set. See:
                `Wynncraft/WynncraftAPI#36 <https://github.com/Wynncraft/WynncraftAPI/issues/36>`_."""
        return self._attributes.get("set", None)

    @property
    def sockets(self) -> int:
        """Number of powder slots this item has."""
        return self._attributes.get("sockets", 0)

    @property
    def armour_type(self) -> Union[ArmourType, None]:
        """Material from which armour is made, if not a armour piece, returns ``None``."""
        if self._attributes.get("armorType", None) is None:
            return None
        else:
            return ArmourType(self._attributes.get("armorType").upper())

    @property
    def armour_color(self) -> Union[Color, None]:
        """Color that this armour piece is dyed. This is only present
        if :py:attr:`armour_type` is :py:attr:`ArmourType.LEATHER` or
        else returns ``None``."""
        if self.armour_type == ArmourType.LEATHER:
            return Color(tuple(int(c) for c in self._attributes.get("armorColor", "160,101,64").split(",")))
        else:
            return None

    @property
    def required_level(self) -> int:
        """Minimum combat level (
        :py:attr:`PlayerProfession.level <corkus.objects.PlayerProfession.level>` from
        :py:attr:`PlayerClass.combat <corkus.objects.PlayerClass.combat>`) required to use this item."""
        return self._attributes.get("level", 1)

    @property
    def required_class(self) -> Union[ClassType, None]:
        """The class that is required for this item to be used.
        ``None`` if item can be used by all classes."""
        if self._attributes.get("classRequirement") is not None:
            return ClassType(self._attributes.get("classRequirement"))
        elif self.type == ItemType.BOW:
            return ClassType.ARCHER
        elif self.type == ItemType.SPEAR:
            return ClassType.WARRIOR
        elif self.type == ItemType.WAND:
            return ClassType.MAGE
        elif self.type == ItemType.DAGGER:
            return ClassType.ASSASSIN
        elif self.type == ItemType.RELIK:
            return ClassType.SKYSEER
        else:
            return None

    @property
    def required_quest(self) -> Union[Quest, None]:
        """The quest that must have been completed in order
        for this item to be used"""
        return self._attributes.get("quest", None)

    @property
    def restrictions(self) -> Union[ItemRestrictions, None]:
        """Restrictions applied to this item."""
        if self._attributes.get("restrictions", None) is None:
            return None
        else:
            return ItemRestrictions(self._attributes.get("restrictions").upper().replace(" ", "_"))

    @property
    def lore(self) -> Union[str, None]:
        """This item's lore."""
        return self._attributes.get("addedLore", None)

    @property
    def item_id(self) -> str:
        """Minecraft `block`_/`item`_ ID + optional `data value`_,
        pre-flattening. Format: ``ID:DV``

        .. _block: https://minecraft.fandom.com/wiki/Java_Edition_data_values/Pre-flattening/Block_IDs
        .. _item: https://minecraft.fandom.com/wiki/Java_Edition_data_values/Pre-flattening/Item_IDs
        .. _data value: https://minecraft.fandom.com/wiki/Java_Edition_data_values/Pre-flattening"""
        return self._attributes.get("material") or self._generate_id()

    def _generate_id(self) -> str:
        if self.armour_type == ArmourType.LEATHER:
            if self.type == ItemType.HELMET:
                return "298:0"
            elif self.type == ItemType.CHESTPLATE:
                return "299:0"
            elif self.type == ItemType.LEGGINGS:
                return "300:0"
            elif self.type == ItemType.BOOTS:
                return "301:0"
        elif self.armour_type == ArmourType.CHAIN:
            if self.type == ItemType.HELMET:
                return "302:0"
            elif self.type == ItemType.CHESTPLATE:
                return "303:0"
            elif self.type == ItemType.LEGGINGS:
                return "304:0"
            elif self.type == ItemType.BOOTS:
                return "305:0"
        elif self.armour_type == ArmourType.IRON:
            if self.type == ItemType.HELMET:
                return "306:0"
            elif self.type == ItemType.CHESTPLATE:
                return "307:0"
            elif self.type == ItemType.LEGGINGS:
                return "308:0"
            elif self.type == ItemType.BOOTS:
                return "309:0"
        elif self.armour_type == ArmourType.DIAMOND:
            if self.type == ItemType.HELMET:
                return "310:0"
            elif self.type == ItemType.CHESTPLATE:
                return "311:0"
            elif self.type == ItemType.LEGGINGS:
                return "312:0"
            elif self.type == ItemType.BOOTS:
                return "313:0"
        elif self.armour_type == ArmourType.GOLDEN:
            if self.type == ItemType.HELMET:
                return "314:0"
            elif self.type == ItemType.CHESTPLATE:
                return "315:0"
            elif self.type == ItemType.LEGGINGS:
                return "316:0"
            elif self.type == ItemType.BOOTS:
                return "317:0"
        return "0:0"

    def __repr__(self) -> str:
        return f"<Item name={self.name!r} type={self.type} tier={self.tier}>"
