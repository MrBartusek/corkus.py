from __future__ import annotations
from enum import Enum

class Timeframe(Enum):
    ALL_TIME = "alltime"
    WEEKLY = "weekly"

class Profession(Enum):
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

    # Crafted
    SCROLL = "SCROLL"
    POTION = "POTION"
    FOOD = "FOOD"
