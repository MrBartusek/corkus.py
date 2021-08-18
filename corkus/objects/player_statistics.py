from __future__ import annotations
from .base import CorkusBase

class ClassStatistics(CorkusBase):
    """General Statistics of a :py:class:`PlayerClass`"""
    @property
    def chests_found(self) -> int:
        """Total chest opened."""
        return self._attributes.get("chestsFound", 0)

    @property
    def blocks_walked(self) -> int:
        """Total blocks walked."""
        return self._attributes.get("blocksWalked", 0)

    @property
    def items_identified(self) -> int:
        """Total items identified.

        .. caution::
                This property is currently bugged and always returns ``0``. See:
                `Wynncraft/WynncraftAPI#62 <https://github.com/Wynncraft/WynncraftAPI/issues/62>`_.
        """
        return self._attributes.get("itemsIdentified", 0)

    @property
    def mobs_killed(self) -> int:
        """Total mobs killed."""
        return self._attributes.get("mobsKilled", 0)

    @property
    def pvp_kills(self) -> int:
        """Total player killed in `The Nether <https://wynncraft.fandom.com/wiki/The_Nether>`_."""
        return self._attributes.get("pvp", {}).get("kills", 0)

    @property
    def pvp_deaths(self) -> int:
        """Total deaths by players in `The Nether <https://wynncraft.fandom.com/wiki/The_Nether>`_."""
        return self._attributes.get("pvp", {}).get("deaths", 0)

    @property
    def deaths(self) -> int:
        """Number of deaths not caused by PVP."""
        return self._attributes.get("deaths", 0)

    @property
    def discoveries(self) -> int:
        """Total number of discoveries by player."""
        return self._attributes.get("discoveries", 0)

    @property
    def swarms_won(self) -> int:
        """Total number of `Swarm Events <https://wynncraft.fandom.com/wiki/Swarm>`_ won by player."""
        return self._attributes.get("eventsWon", 0)

    @property
    def logins(self) -> int:
        """Number of logins to the server."""
        return self._attributes.get("deaths", 0)

    def __repr__(self) -> str:
        return f"<ClassStatistics chests_found={self.chests_found} mobs_killed={self.mobs_killed}>"

class PlayerStatistics(ClassStatistics):
    """General Statistics of a :py:class:`Player`. This class is based on :py:class:`ClassStatistics`."""
    @property
    def total_combat_level(self) -> int:
        """Sum of combat level across all classes."""
        return self._attributes.get("totalLevel", {}).get("combat", 0)

    @property
    def total_profession_level(self) -> int:
        """Sum of profession level across all classes."""
        return self._attributes.get("totalLevel", {}).get("profession", 0)

    def __repr__(self) -> str:
        return f"<PlayerStatistics chests_found={self.chests_found} mobs_killed={self.mobs_killed}>"
