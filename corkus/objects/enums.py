from __future__ import annotations
from enum import Enum

class Timeframe(Enum):
    """List of timeframes available for some of leaderboard endpoints."""

    ALL_TIME = "alltime"
    WEEKLY = "weekly"

class LogicSymbol(Enum):
    """LogicSymbols are use in more advanced search calls in the API.

    .. py:currentmodule:: corkus.objects

    If you want to search for :py:class:`Ingredient` that require
    :py:attr:`ProfessionType.ARMOURING` AND :py:attr:`ProfessionType.SCRIBING` at the same time,
    you use :py:attr:`AND`

    If you want to search for :py:class:`Ingredient` that require
    :py:attr:`ProfessionType.ARMOURING` OR :py:attr:`ProfessionType.SCRIBING`
    you use :py:attr:`OR`. It will result all of the results that
    have any of provided skills."""

    AND = "&"
    """Return list of results that match **ALL OF THE PROVIDED ARGUMENTS**."""

    OR = "^"
    """Return list of results that match **ONE OR MORE OF THE PROVIDED ARGUMENTS**."""


class ProfessionType(Enum):
    """List of Gathering and Crafting `Professions <https://wynncraft.fandom.com/wiki/Professions>`_ plus :py:attr:`COMBAT`."""

    COMBAT = "COMBAT"
    ALCHEMISM = "ALCHEMISM"
    ARMOURING = "ARMOURING"
    COOKING = "COOKING"
    JEWELING = "JEWELING"
    SCRIBING = "SCRIBING"
    TAILORING = "TAILORING"
    WEAPONSMITHING = "WEAPONSMITHING"
    WOODWORKING = "WOODWORKING"
    MINING = "MINING"
    WOODCUTTING = "WOODCUTTING"
    FARMING = "FARMING"
    FISHING = "FISHING"

class ItemType(Enum):
    """Crafted and regular items."""

    HELMET = "HELMET"
    CHESTPLATE = "CHESTPLATE"
    LEGGINGS = "LEGGINGS"
    BOOTS = "BOOTS"
    RING = "RING"
    NECKLACE = "NECKLACE"
    BRACELET = "BRACELET"
    DAGGER = "DAGGER"
    SPEAR = "SPEAR"
    BOW = "BOW"
    WAND = "WAND"
    RELIK = "RELIK"

    SCROLL = "SCROLL"
    """Crafted item."""
    POTION = "POTION"
    """Crafted item."""
    FOOD = "FOOD"
    """Crafted item."""

class ItemCategory(Enum):
    """Crafted and regular items."""

    ARMOUR = "ARMOUR"
    WEAPON = "WEAPON"
    ACCESSORY = "ACCESSORY"
    COMSUMABLE = "COMSUMABLE"

    @staticmethod
    def from_type(type: ItemType) -> "ItemCategory":
        """Convert :py:class:`ItemType` intro :py:class:`ItemCategory`."""
        if type in (ItemType.HELMET, ItemType.CHESTPLATE, ItemType.LEGGINGS, ItemType.BOOTS):
            return ItemCategory.ARMOUR
        elif type in (ItemType.RING, ItemType.NECKLACE, ItemType.BRACELET):
            return ItemCategory.ACCESSORY
        elif type in (ItemType.DAGGER, ItemType.SPEAR, ItemType.BOW, ItemType.WAND, ItemType.RELIK):
            return ItemCategory.WEAPON
        elif type in (ItemType.SCROLL, ItemType.POTION, ItemType.FOOD):
            return ItemCategory.COMSUMABLE
        else:
            raise ValueError(f"invalid type: {type}")
