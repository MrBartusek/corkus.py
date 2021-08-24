from __future__ import annotations
from typing import TYPE_CHECKING
from enum import Enum
from .base import CorkusBase

if TYPE_CHECKING:
    from corkus import Corkus

class HardcoreType(Enum):
    """Describes current status of player's hardcore challenge."""
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"
    FAILED = "FAILED"

class PlayerGamemodes(CorkusBase):
    """Challenge gamemodes that are enabled on a :py:class:`PlayerClass`."""
    def __init__(self, corkus: Corkus, attributes: dict, deaths: int):
        super().__init__(corkus, attributes)
        self._deaths = deaths

    @property
    def craftsman(self) -> str:
        """Does this class have the craftsman challenge enabled."""
        return self._attributes.get("craftsman", False)

    @property
    def hardcore(self) -> HardcoreType:
        """Does this class have the hardcore challenge enabled and what is the status of it."""
        enabled = self._attributes.get("hardcore", False)
        active = self._deaths <= 0
        if enabled and active:
            return HardcoreType.ENABLED
        elif enabled and not active:
            return HardcoreType.FAILED
        else:
            return HardcoreType.DISABLED

    @property
    def ironman(self) -> bool:
        """Does this class have the ironman challenge enabled."""
        return self._attributes.get("ironman", False)

    @property
    def hunted(self) -> bool:
        """Does this class have the haunted mode enabled."""
        return self._attributes.get("hunted", False)

    def __repr__(self) -> str:
        return f"<Gamemodes craftsman={self.craftsman!r} hardcore={self.hardcore!r} ironman={self.ironman!r} hunted={self.hunted!r}>"
