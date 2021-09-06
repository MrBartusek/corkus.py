from __future__ import annotations
from corkus.objects.identification_type import IdentificationType
from typing import List, Union
from enum import Enum
import base64
import json
import math

from .base import CorkusBase
from corkus.utils import CorkusEnum
from .enums import ItemType, ItemCategory
from .player_class import ClassType
from .color import Color
from .quest import Quest
from .weapon_damage import WeaponDamage
from .skill_points import SkillPoints
from .armour_defense import ArmourDefence
from .major_identification import MajorIdentification
from .mojang_skin_response import MojangSkinResponse
from .identification_values import IdentificationValues
from .identification import Identification

class ItemTier(CorkusEnum):
    """Rarity tier of the item."""

    MYTHIC = "MYTHIC"
    FABLED = "FABLED"
    LEGENDARY = "LEGENDARY"
    RARE = "RARE"
    UNIQUE = "UNIQUE"
    SET = "SET"
    NORMAL = "NORMAL"

class ArmourType(CorkusEnum):
    """Material from which armour is made, same as in vanilla."""

    DIAMOND = "DIAMOND"
    GOLDEN = "GOLDEN"
    CHAIN = "CHAIN"
    IRON = "IRON"
    LEATHER = "LEATHER"

class ItemRestrictions(Enum):
    """Restrictions applied to some items."""

    UNTRADABLE = "UNTRADABLE"
    """Items that cannot be traded or dropped."""

    QUEST_ITEM = "QUEST_ITEM"
    """A special kind of :py:attr:`UNTRADABLE` items awarded during
    or after completing a quest."""

class AttackSpeed(CorkusEnum):
    """Attack speed of a weapon."""

    SUPER_FAST = "SUPER_FAST"
    VERY_FAST = "VERY_FAST"
    FAST = "FAST"
    NORMAL = "NORMAL"
    SLOW = "SLOW"
    SUPER_SLOW = "SUPER_SLOW"
    VERY_SLOW = "VERY_SLOW"

class Item(CorkusBase):
    """Represents regular (non-crafted) Wynncraft item."""
    @property
    def name(self) -> str:
        """The name of the item."""
        return self._attributes.get("name", "")

    @property
    def display_name(self) -> str:
        """Name that should be displayed to end-user, usually match :py:attr:`name`.

        .. caution::
            This property may not be reliable. See:
            `Wynncraft/WynncraftAPI19 <https://github.com/Wynncraft/WynncraftAPI/issues/19>`_.
        """
        return self._attributes.get("displayName", self.name)

    @property
    def type(self) -> ItemType:
        """Type of the item."""
        return ItemType(self._attributes.get("type", self._attributes.get("accessoryType", "Wand")).upper())

    @property
    def category(self) -> ItemCategory:
        """Category of the item."""
        return ItemCategory.from_type(self.type)

    @property
    def tier(self) -> ItemTier:
        """Item rarity tier."""
        return ItemTier(self._attributes.get("tier", "Normal").upper())

    @property
    def set(self) -> Union[str, None]:
        """The name of the set this item is part of. ``None`` if not part of a set.

        .. caution::
                This property is currently bugged and works only for ``Leaf`` set. See:
                `Wynncraft/WynncraftAPI#36 <https://github.com/Wynncraft/WynncraftAPI/issues/36>`_."""
        return self._attributes.get("set", None)

    @property
    def sockets(self) -> int:
        """Number of powder slots this item has."""
        return self._attributes.get("sockets", 0)

    @property
    def armour_type(self) -> Union[ArmourType, None]:
        """Material from which armour is made. If not a armour piece, or
        item is player head, returns ``None``."""
        if self.skin is not None:
            return None
        elif self._attributes.get("armorType", None) is None:
            return None
        else:
            return ArmourType(self._attributes.get("armorType").upper())

    @property
    def armour_color(self) -> Union[Color, None]:
        """Color that this armour piece is dyed. This is only present
        if :py:attr:`armour_type` is :py:attr:`ArmourType.LEATHER` or
        else returns ``None``."""
        if self.armour_type == ArmourType.LEATHER:
            return Color(tuple(int(c) for c in self._attributes.get("armorColor", "160,101,64").split(",")))
        else:
            return None

    @property
    def required_level(self) -> int:
        """Minimum combat level
        (:py:attr:`PlayerProfession.level <corkus.objects.PlayerProfession.level>` from
        :py:attr:`PlayerClass.combat <corkus.objects.PlayerClass.combat>`) required to use this item."""
        return self._attributes.get("level", 1)

    @property
    def required_class(self) -> Union[ClassType, None]:
        """The class that is required for this item to be used.
        ``None`` if item can be used by all classes."""
        if self._attributes.get("classRequirement") is not None:
            return ClassType(self._attributes.get("classRequirement").upper())
        elif self.type == ItemType.BOW:
            return ClassType.ARCHER
        elif self.type == ItemType.SPEAR:
            return ClassType.WARRIOR
        elif self.type == ItemType.WAND:
            return ClassType.MAGE
        elif self.type == ItemType.DAGGER:
            return ClassType.ASSASSIN
        elif self.type == ItemType.RELIK:
            return ClassType.SKYSEER
        else:
            return None

    @property
    def skill_points(self) -> SkillPoints:
        """Skill points required in order to use this item."""
        return SkillPoints(
            corkus = self._corkus,
            strength = self._attributes.get("strength", 0),
            dexterity = self._attributes.get("dexterity", 0),
            intelligence = self._attributes.get("intelligence", 0),
            defence = self._attributes.get("defence", 0),
            agility = self._attributes.get("agility", 0)
        )

    @property
    def required_quest(self) -> Union[Quest, None]:
        """The quest that must have been completed in order
        for this item to be used."""
        return self._attributes.get("quest", None)

    @property
    def restrictions(self) -> Union[ItemRestrictions, None]:
        """Restrictions applied to this item."""
        if self._attributes.get("restrictions", None) is None:
            return None
        else:
            return ItemRestrictions(self._attributes.get("restrictions").upper().replace(" ", "_"))

    @property
    def lore(self) -> Union[str, None]:
        """This item's lore."""
        return self._attributes.get("addedLore", None)

    @property
    def damage(self) -> Union[WeaponDamage, None]:
        """If this item is a weapon (:py:attr:`category` is :py:attr:`ItemCategory.WEAPON`)
        return it's damage."""
        if self.category is ItemCategory.WEAPON:
            return WeaponDamage(self._corkus, self._attributes)
        else:
            return None

    @property
    def attack_speed(self) -> Union[AttackSpeed, None]:
        """If this item is a weapon (:py:attr:`category` is :py:attr:`ItemCategory.WEAPON`)
        return it's attack speed."""
        if self.category is ItemCategory.WEAPON:
            return AttackSpeed(self._attributes.get("attackSpeed", "VERY_SLOW"))
        else:
            return None

    @property
    def identified(self) -> bool:
        """Is this item is pre-identified when obtained."""
        return self._attributes.get("identified", False)

    @property
    def health(self) -> Union[AttackSpeed, None]:
        """If this item is a armour piece (:py:attr:`category` is :py:attr:`ItemCategory.ARMOUR`)
        return set amount of health this armor provides."""
        if self.category is ItemCategory.ARMOUR:
            return self._attributes.get("health", 0)
        else:
            return None

    @property
    def armour_defence(self) -> Union[ArmourDefence, None]:
        """If this item is a armour piece (:py:attr:`category` is :py:attr:`ItemCategory.ARMOUR`)
        return protection it gives against elemental attacks."""
        if self.category is ItemCategory.ARMOUR:
            return ArmourDefence(self._corkus, self._attributes)
        else:
            return None

    @property
    def major_identifications(self) -> List[MajorIdentification]:
        """List all Major IDs on the item."""
        return [MajorIdentification(self._corkus, i) for i in self._attributes.get("majorIds", [])]

    @property
    def identifications(self) -> List[Identification]:
        """List all identifications of this item."""
        not_identified_id = (
            IdentificationType.AIR_DEFENSE,
            IdentificationType.FIRE_DEFENSE,
            IdentificationType.EARTH_DEFENSE,
            IdentificationType.WATER_DEFENSE,
            IdentificationType.THUNDER_DEFENSE
        )

        result = []
        for key, value in self._attributes.items():
            if not isinstance(value, int) or value == 0: continue
            type = IdentificationType.from_items_api(key)
            if type is None: continue
            if self.identified or type in not_identified_id:
                result.append(Identification(self._corkus, type, value = value))
            else:
                result.append(Identification(self._corkus, type, values = self._generate_identification_value(value)))
        return result

    def _generate_identification_value(self, base_value: int) -> IdentificationValues:
        """The values given by the API represent the 'base value' of that identification, when an item is
        actually identified a random number is generated for each non-zero identification and is then
        multiplied by that identification's base value. For identifications that have a positive base
        value, the random number can be between 0.3 and 1.3. For identifications that have a negative
        base value, the random number can be between 0.7 and 1.3. The result after multiplication is then
        rounded to the nearest integer, with a maximum value of -1 for negative identifications and a
        minimum value of 1 for positive identifications.
        """
        min_value, max_value = None, None
        if base_value > 0:
            min_value = max(self._normal_round(base_value * 0.3), 1)
            max_value = max(self._normal_round(base_value * 1.3), 1)
        else:
            min_value = min(self._normal_round(base_value * 0.7), -1)
            max_value = min(self._normal_round(base_value * 1.3), -1)
        return IdentificationValues(
            self._corkus,
            min = min_value,
            max = max_value
        )

    def _normal_round(self, n):
        if n - math.floor(n) < 0.5:
            return math.floor(n)
        return math.ceil(n)

    @property
    def skin(self) -> Union[MojangSkinResponse, None]:
        """If this item is a helmet (:py:attr:`type` is :py:attr:`ItemType.HELMET`)
        in form player head, this return information about owner of the head."""
        if self._attributes.get("skin") is not None:
            response = base64.b64decode(self._attributes.get("skin"))
            attributes = json.loads(response)
            return MojangSkinResponse(self._corkus, attributes)
        else:
            return None

    @property
    def item_id(self) -> str:
        """Minecraft `block`_/`item`_ ID + optional `data value`_,
        pre-flattening. Format: ``ID:DV``

        .. _block: https://minecraft.fandom.com/wiki/Java_Edition_data_values/Pre-flattening/Block_IDs
        .. _item: https://minecraft.fandom.com/wiki/Java_Edition_data_values/Pre-flattening/Item_IDs
        .. _data value: https://minecraft.fandom.com/wiki/Java_Edition_data_values/Pre-flattening"""
        if self.skin is not None:
            return "397:3"

        return self._attributes.get("material") or self._generate_id()

    def _generate_id(self) -> str:
        if self.armour_type == ArmourType.LEATHER:
            if self.type == ItemType.HELMET:
                return "298:0"
            elif self.type == ItemType.CHESTPLATE:
                return "299:0"
            elif self.type == ItemType.LEGGINGS:
                return "300:0"
            elif self.type == ItemType.BOOTS:
                return "301:0"
        elif self.armour_type == ArmourType.CHAIN:
            if self.type == ItemType.HELMET:
                return "302:0"
            elif self.type == ItemType.CHESTPLATE:
                return "303:0"
            elif self.type == ItemType.LEGGINGS:
                return "304:0"
            elif self.type == ItemType.BOOTS:
                return "305:0"
        elif self.armour_type == ArmourType.IRON:
            if self.type == ItemType.HELMET:
                return "306:0"
            elif self.type == ItemType.CHESTPLATE:
                return "307:0"
            elif self.type == ItemType.LEGGINGS:
                return "308:0"
            elif self.type == ItemType.BOOTS:
                return "309:0"
        elif self.armour_type == ArmourType.DIAMOND:
            if self.type == ItemType.HELMET:
                return "310:0"
            elif self.type == ItemType.CHESTPLATE:
                return "311:0"
            elif self.type == ItemType.LEGGINGS:
                return "312:0"
            elif self.type == ItemType.BOOTS:
                return "313:0"
        elif self.armour_type == ArmourType.GOLDEN:
            if self.type == ItemType.HELMET:
                return "314:0"
            elif self.type == ItemType.CHESTPLATE:
                return "315:0"
            elif self.type == ItemType.LEGGINGS:
                return "316:0"
            elif self.type == ItemType.BOOTS:
                return "317:0"
        return "0:0"

    def __repr__(self) -> str:
        return f"<Item name={self.name!r} type={self.type} tier={self.tier}>"
