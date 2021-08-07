from __future__ import annotations
from typing import TYPE_CHECKING
from enum import Enum
from .base import CorkusBase

if TYPE_CHECKING:
    from corkus import Corkus

class HardcoreType(Enum):
    ENABLED = "Enabled"
    DISABLED = "Disabled"
    FAILED = "Failed"

class PlayerGamemodes(CorkusBase):
    def __init__(self, corkus: Corkus, attributes: dict, deaths: int):
        super().__init__(corkus, attributes)
        self._deaths = deaths

    @property
    def craftsman(self) -> str:
        """Does this class have the craftsman challenge enabled"""
        return self.attributes.get("craftsman", False)

    @property
    def hardcore(self) -> HardcoreType:
        """Does this class have the hardcore challenge enabled and what is the status of it"""
        enabled = self.attributes.get("hardcore", False)
        active = self._deaths <= 0
        if enabled and active:
            return HardcoreType.ENABLED
        elif enabled and not active:
            return HardcoreType.FAILED
        else:
            return HardcoreType.DISABLED

    @property
    def ironman(self) -> bool:
        """Does this class have the ironman challenge enabled"""
        return self.attributes.get("ironman", False)

    @property
    def hunted(self) -> bool:
        """Does this class have the haunted mode enabled"""
        return self.attributes.get("hunted", False)

    def __repr__(self) -> str:
        return f"<Gamemodes craftsman={self.craftsman!r} hardcore={self.hardcore!r} ironman={self.ironman!r} hunted={self.hunted!r}>"