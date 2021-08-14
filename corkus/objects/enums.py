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
    """A special kind of :py:attr:`UNTRADEABLE` items awarded during
    or after completing a quest."""
