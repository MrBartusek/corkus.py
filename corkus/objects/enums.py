from __future__ import annotations
from enum import Enum

class Timeframe(Enum):
    """List of timeframes available for some of leaderboard endpoints."""

    ALL_TIME = "alltime"
    WEEKLY = "weekly"

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

    # Crafted
    SCROLL = "SCROLL"
    POTION = "POTION"
    FOOD = "FOOD"
