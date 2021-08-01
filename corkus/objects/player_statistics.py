from __future__ import annotations
from typing import TYPE_CHECKING
from .base import CorkusBase

if TYPE_CHECKING:
    from corkus import Corkus
    from corkus.objects import Player

class PlayerStatistics(CorkusBase):
    @property
    def chests_found(self):
        """Total chest opened"""
        return self.attributes.get("chestsFound", 0)

    @property
    def blocksWalked(self):
        """Total blocks walked"""
        return self.attributes.get("blocksWalked", 0)

    @property
    def items_identified(self):
        """Total items identified"""
        return self.attributes.get("itemsIdentified", 0)

    @property
    def mobs_killed(self):
        """Total mobs killed"""
        return self.attributes.get("mobsKilled", 0)

    @property
    def total_combat_level(self):
        """Sum of combat level across all classes"""
        return self.attributes.get("totalLevel", {}).get("combat", 0)

    @property
    def total_profession_level(self):
        """Sum of profession level across all classes"""
        return self.attributes.get("totalLevel", {}).get("profession", 0)

    @property
    def pvp_kills(self):
        """Total player killed in [The Nether](https://wynncraft.fandom.com/wiki/The_Nether)"""
        return self.attributes.get("pvp", {}).get("kills", 0)

    @property
    def pvp_deaths(self):
        """Total deaths by players [The Nether](https://wynncraft.fandom.com/wiki/The_Nether)"""
        return self.attributes.get("pvp", {}).get("deaths", 0)

    @property
    def logins(self):
        """Number of Logins to the server"""
        return self.attributes.get("deaths", 0)

    @property
    def deaths(self):
        """Number of deaths not caused by PVP"""
        return self.attributes.get("deaths", 0)

    @property
    def discoveries(self):
        """Total number of Discoveries"""
        return self.attributes.get("discoveries", 0)

    @property
    def swarms_won(self):
        """Total number of [Swarm Events](https://wynncraft.fandom.com/wiki/Swarm) won by player"""
        return self.attributes.get("eventsWon", 0)

    def __repr__(self) -> str:
        return f"<PlayerStatistics chests_found={self.chests_found} mobs_killed={self.mobs_killed}>"
