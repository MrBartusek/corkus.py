from __future__ import annotations
from .base import CorkusBase
from enum import Enum

class DungeonType(Enum):
    REMOVED = "REMOVED"
    """Dungeons that were removed from the game in version ``1.14.1`` like ``Skeleton`` or ``Spider``"""

    REMOVED_MINI = "REMOVED_MINI"
    """Minidungeons that were reworked in version ``1.17`` like ``Ice`` or ``Ocean``"""

    STANDARD = "STANDARD"
    """Generic dungeons like ``Galleon's Graveyard`` or ``Fallen Factory``"""

    CORRUPTED = "CORRUPTED"
    """Harder variant of standard dungeons like ``Corrupted Decrepit Sewers`` or ``Corrupted Sand-Swept Tomb``"""

class Dungeon(CorkusBase):
    """Represents a `Dungeon <https://wynncraft.fandom.com/wiki/Dungeons>`_ completed by a :py:class:`Player`"""
    @property
    def name(self) -> str:
        """Name of the dungeon  like ``Decrepit Sewers``, ``Galleon's Graveyard`` or ``Fallen Factory``."""
        return self._attributes.get("name", "")

    @property
    def type(self) -> DungeonType:
        """Type of the dungeon."""
        if self.name.startswith("Corrupted"):
            return DungeonType.CORRUPTED
        elif self.name in (
            "Zombie",
            "Animal",
            "Skeleton",
            "Spider",
            "Silverfish",):
            return DungeonType.REMOVED
        elif self.name in (
            "Jungle",
            "Ice",
            "Ocean"):
            return DungeonType.REMOVED_MINI
        elif self.name in (
            "Decrepit Sewers",
            "Infested Pit",
            "Ice Barrows",
            "Lost Sanctuary",
            "Sand-Swept Tomb",
            "Underworld Crypt",
            "Undergrowth Ruins",
            "Eldritch Outlook",
            "Galleon's Graveyard",
            "Fallen Factory"):
            return DungeonType.STANDARD
        else:
            raise ValueError(f"Invalid dungeon: {self.name}")

    @property
    def completed(self) -> int:
        """Total runs completed by the player. Failed runs are not counted."""
        return self._attributes.get("completed", 0)

    def __repr__(self) -> str:
        return f"<Dungeon name={self.name!r} completed={self.completed}>"
