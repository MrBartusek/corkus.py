from __future__ import annotations
from corkus.objects.base import CorkusBase
from typing import TYPE_CHECKING, Literal, List
from enum import Enum

if TYPE_CHECKING:
    from .guild import Guild

class Profession(Enum):
    ALCHEMISM = "ALCHEMISM"
    ARMOURING = "ARMOURING"
    COOKING = "COOKING"
    JEWELING = "JEWELING"
    SCRIBING = "SCRIBING"
    TAILORING = "TAILORING"
    WEAPONSMITHING = "WEAPONSMITHING"
    WOODWORKING = "WOODWORKING"

class Ingredient(CorkusBase):
    @property
    def name(self) -> str:
        """The name of the ingredient"""
        return self.attributes.get("name", "")

    @property
    def tier(self) -> Literal[0, 1, 2, 3]:
        """Number of stars on the ingredient"""
        return self.attributes.get("tier", 0)

    @property
    def reqired_level(self) -> int:
        """Level that an player must get on all of the :py:attr:`~reqired_professions` in order to use this ingredient"""
        return self.attributes.get("level", 0)

    @property
    def reqired_professions(self) -> List[Profession]:
        """List of professions on which player must get :py:attr:`~reqired_level` in order to use this ingredient"""
        raise NotImplementedError

    @property
    def sprite(self):
        raise NotImplementedError

    @property
    def identifications(self):
        raise NotImplementedError

    @property
    def position_modifiers(self):
        raise NotImplementedError

    @property
    def item_modifiers(self):
        raise NotImplementedError

    @property
    def consumable_modifiers(self):
        raise NotImplementedError

    def __repr__(self) -> str:
        return f"<Ingredient name={self.name!r}>"
