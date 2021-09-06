from __future__ import annotations
from .partial_base import PartialBase

class SkillPoints(PartialBase):
    """This is multi-purpose class for player skill points. You may see it as a reqired
    skill points for an item or skill points of the class."""

    def __init__(self, corkus, strength: int, dexterity: int, intelligence: int, defence: int, agility: int) -> None:
        super().__init__(corkus)
        self._strength = strength
        self._dexterity = dexterity
        self._intelligence = intelligence
        self._defence = defence
        self._agility = agility

    @property
    def strength(self) -> int:
        return self._strength

    @property
    def dexterity(self) -> int:
        return self._dexterity

    @property
    def intelligence(self) -> int:
        return self._intelligence

    @property
    def defence(self) -> int:
        return self._defence

    @property
    def agility(self) -> int:
        return self._agility

    def __repr__(self) -> str:
        return f"<SkillPoints strength={self.strength} dexterity={self.dexterity} intelligence={self.intelligence} defence={self.defence} agility={self.agility}>"
