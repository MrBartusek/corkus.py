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
