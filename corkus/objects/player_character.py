from __future__ import annotations
from datetime import datetime, timezone
from enum import Enum
from typing import TYPE_CHECKING, List, Tuple
from corkus.objects.base_player import PlayerTag
from corkus.objects.uuid import CorkusUUID

from .base import CorkusBase
from .player_profession import PlayerProfession
from .quest import Quest
from .player_statistics import ClassStatistics
from .player_gamemodes import HardcoreType, PlayerGamemodes
from .dungeon import Dungeon, DungeonType
from .raid import Raid
from .enums import ProfessionType
from .skill_points import SkillPoints
from .playtime import PlayerPlaytime

if TYPE_CHECKING:
    from corkus import Corkus
    from .player import Player

class CharacterType(Enum):
    """Type of :py:class:`Character`."""
    ARCHER = "ARCHER"
    WARRIOR = "WARRIOR"
    MAGE = "MAGE"
    ASSASSIN = "ASSASSIN"
    SHAMAN = "SHAMAN"

    HUNTER = "HUNTER"
    KNIGHT = "KNIGHT"
    DARK_WIZARD = "DARKWIZARD"
    NINJA = "NINJA"
    SKYSEER = "SKYSEER"

class Character(CorkusBase):
    """Represents one of the player's characters that a :py:class:`Player` have currently active."""
    def __init__(self, corkus: Corkus, player: Player, uuid: str, attributes: dict):
        self._player = player
        self._uuid = uuid
        super().__init__(corkus, attributes)

    @property
    def uuid(self) -> CorkusUUID:
        """Unique identifier for this character."""
        return CorkusUUID(self._uuid)

    @property
    def display_name(self) -> str:
        """Pretty name to display to end-user like ``Archer``, ``Mage`` or ``Dark Wizard``."""
        if self.type == CharacterType.DARK_WIZARD:
            return "Dark Wizard"
        return self.type.value.title()

    @property
    def approximate_create(self) -> Tuple[datetime, datetime]:
        """Approximate time when class was created.

        .. note::
            Wynncraft API does not provide information about
            when a class was created. This property makes a educated guess and provide two datetimes
            between which this class was created.
        """
        SE_UPDATE = datetime(2019, 12, 8, tzinfo = timezone.utc)
        ECONOMY_UPDATE_PATCH1 = datetime(2019, 6, 8, tzinfo = timezone.utc)
        ECONOMY_UPDATE = datetime(2019, 1, 18, tzinfo = timezone.utc)
        DUNGEONS_UPDATE = datetime(2017, 12, 15, tzinfo = timezone.utc)
        GAMEPLAY_UPDATE = datetime(2016, 8, 28, tzinfo = timezone.utc)
        MOB_UPDATE = datetime(2014, 8, 1, tzinfo = timezone.utc)

        start = self._player.join_date
        end = self._player.last_online

        if self.kind == CharacterType.SHAMAN:
            start = max(SE_UPDATE, start)

        if self.reskinned and self._player.tag not in (PlayerTag.HERO, PlayerTag.CHAMPION):
            start = max(SE_UPDATE, start)

        if self.pre_economy_update or self.statistics.pvp_deaths > 0 or self.statistics.pvp_kills > 0:
            end = min(ECONOMY_UPDATE, end)

        if self.gamemode.craftsman or self.gamemode.hardcore != HardcoreType.DISABLED or self.gamemode.ironman:
            start = max(ECONOMY_UPDATE_PATCH1, start)

        if self.gamemode.hunted:
            start = max(SE_UPDATE, start)

        if any(d.type == DungeonType.REMOVED_MINI for d in self.dungeons):
            end = min(DUNGEONS_UPDATE, end)

        if any(d.type == DungeonType.REMOVED for d in self.dungeons):
            end = min(GAMEPLAY_UPDATE, end)

        if self.statistics.swarms_won > 0:
            end = min(MOB_UPDATE, end)

        return (start, end)

    @property
    def kind(self) -> CharacterType:
        """Class type ignoring re-skinned variants. :py:attr:`CharacterType.DARK_WIZARD` is converted to :py:attr:`CharacterType.MAGE` etc."""
        class_type = self.type
        if class_type == CharacterType.HUNTER:
            return CharacterType.ARCHER
        elif class_type == CharacterType.KNIGHT:
            return CharacterType.WARRIOR
        elif class_type == CharacterType.DARK_WIZARD:
            return CharacterType.MAGE
        elif class_type == CharacterType.NINJA:
            return CharacterType.ASSASSIN
        elif class_type == CharacterType.SKYSEER:
            return CharacterType.SHAMAN
        else:
            return class_type

    @property
    def reskinned(self) -> bool:
        """Does this class use re-skinned variant."""
        return self.type != self.kind

    @property
    def type(self) -> CharacterType:
        """Class type including re-skinned variants."""
        return CharacterType(self._attributes.get("type", ""))

    @property
    def quests(self) -> List[Quest]:
        """List of all quests completed by player on this class."""
        return [Quest(self._corkus, q) for q in self._attributes.get("quests", {}).get("list", [])]

    @property
    def playtime(self) -> PlayerPlaytime:
        """Time that player spent on wynncraft servers using this class."""
        return PlayerPlaytime(self._attributes.get("playtime", 0))

    @property
    def combined_level(self) -> int:
        """Combined level of all professions including combat."""
        return self._attributes.get("level", 0)

    @property
    def statistics(self) -> ClassStatistics:
        """General statistics for this class."""
        return ClassStatistics(self._corkus, self._attributes)

    @property
    def skill_points(self) -> SkillPoints:
        """Skill points of this class."""
        skills = self._attributes.get("skills", {})
        return SkillPoints(
            corkus = self._corkus,
            strength = skills.get("strength", 0),
            dexterity = skills.get("dexterity", 0),
            intelligence = skills.get("intelligence", 0),
            defence = skills.get("defence", 0),
            agility = skills.get("agility", 0)
        )

    @property
    def dungeons(self) -> List[Dungeon]:
        """List of dungeons completed by this class."""
        return [Dungeon(self._corkus, d) for d in self._attributes.get("dungeons", {}).get("list", [])]

    @property
    def raids(self) -> List[Raid]:
        """List of raids completed by this class."""
        return [Raid(self._corkus, d) for d in self._attributes.get("raids", {}).get("list", [])]

    @property
    def gamemode(self) -> PlayerGamemodes:
        """Challenge gamemodes that are enabled on this class."""
        return PlayerGamemodes(self._corkus, self._attributes.get("gamemode", {}), self.statistics.deaths)

    @property
    def professions(self) -> List[PlayerProfession]:
        """Returns a list of all players professions."""
        return [PlayerProfession(self._corkus, name, attr) for name, attr in self._attributes.get("professions", {}).items()]

    @property
    def combat(self) -> PlayerProfession:
        """Shortcut to combat profession."""
        return self.get_profession(ProfessionType.COMBAT)

    @property
    def pre_economy_update(self) -> str:
        """Did this class achieve level 101 before `1.18 Economy Update
        <https://forums.wynncraft.com/threads/1-18-the-economy-update-changelog.238340/>`_
        when level cap was risen.
        """
        return self._attributes.get("preEconomyUpdate")

    def get_profession(self, profession: ProfessionType) -> PlayerProfession:
        """Returns a profession with the given profession type.

        :param profession: Type of profession."""
        return next((p for p in self.professions if p.type == profession), None)

    def __repr__(self) -> str:
        return f"<Character type={self.display_name!r} combat={self.combat.level}>"
