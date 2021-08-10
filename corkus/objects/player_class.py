from __future__ import annotations
from enum import Enum
from typing import List, Literal
from .base import CorkusBase
from .quest import Quest
from .player_statistics import ClassStatistics
from .player_gamemodes import PlayerGamemodes
from .dungeon import Dungeon
from .raid import Raid

class ClassType(Enum):
    ARCHER = "Archer"
    WARRIOR = "Warrior"
    MAGE = "Mage"
    ASSASSIN = "Assassin"
    SHAMAN = "Shamman"

    HUNTER = "Hunter"
    KNIGHT = "Knight"
    DARK_WIZARD = "Dark Wizard"
    NINJA = "Ninja"
    SKYSEER = "Skyseer"

class PlayerClass(CorkusBase):
    @property
    def name(self):
        """The official name of the class for example: `mage`, `knight1`, `darkwizard3`"""
        return self._attributes.get("name", "")

    @property
    def display_name(self) -> Literal["Archer", "Warrior", "Mage", "Assassin", "Shamman", "Hunter", "Knight", "Dark Wizard", "Ninja", "Skyseer"]:
        """Pretty name to display to end-user"""
        return self.type.value

    @property
    def kind(self) -> ClassType:
        """Class type ignoring re-skinned variants. `DARK_WIZARD` is converted to `MAGE` etc."""
        class_type = self.type
        if class_type == ClassType.HUNTER:
            return ClassType.ARCHER
        elif class_type == ClassType.KNIGHT:
            return ClassType.WARRIOR
        elif class_type == ClassType.DARK_WIZARD:
            return ClassType.MAGE
        elif class_type == ClassType.NINJA:
            return ClassType.ASSASSIN
        elif class_type == ClassType.SKYSEER:
            return ClassType.SHAMAN
        else:
            return class_type

    @property
    def type(self) -> ClassType:
        """Class type including re-skinned variants"""
        name = "".join([i for i in self.name if not i.isdigit()])
        if name == "darkwizard":
            name = "dark wizard"
        name = name.capitalize()
        return ClassType(name)

    @property
    def quests(self) -> List[Quest]:
        """List of all quests completed by player on this class"""
        return [Quest(self._corkus, q) for q in self._attributes.get("quests", {}).get("list", [])]

    @property
    def statistics(self) -> ClassStatistics:
        """General statistics across for this class"""
        return ClassStatistics(self._corkus, self._attributes)

    @property
    def dungeons(self) -> List[Dungeon]:
        """List of dungeons completed by this class"""
        return [Dungeon(self._corkus, d) for d in self._attributes.get("dungeons", {}).get("list", [])]

    @property
    def raids(self) -> List[Raid]:
        """List of raids completed by this class"""
        return [Dungeon(self._corkus, d) for d in self._attributes.get("raids", {}).get("list", [])]

    @property
    def gamemode(self):
        """The challenge gamemodes that are enabled on this class"""
        return PlayerGamemodes(self._corkus, self._attributes.get("gamemode", {}), self.statistics.deaths)

    @property
    def professions(self):
        raise NotImplementedError

    @property
    def combat(self):
        raise NotImplementedError

    def __repr__(self) -> str:
        return f"<PlayerClass type={self.display_name!r}>"
