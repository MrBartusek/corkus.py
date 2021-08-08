from __future__ import annotations
from .base import CorkusBase

class IngredientItemModifiers(CorkusBase):
    @property
    def durability(self) -> int:
        """Modifier on item durability"""
        return self._attributes.get("durabilityModifier", 0)

    @property
    def strength_required(self) -> int:
        """Number of required strength skill points added to the item"""
        return self._attributes.get("strengthRequirement", 0)

    @property
    def dexterity_required(self) -> int:
        """Number of required dexterity skill points added to the item"""
        return self._attributes.get("dexterityRequirement", 0)

    @property
    def intelligence_required(self) -> int:
        """Number of required intelligence skill points added to the item"""
        return self._attributes.get("intelligenceRequirement", 0)

    @property
    def defence_required(self) -> int:
        """Number of required defence skill points added to the item"""
        return self._attributes.get("defenceRequirement", 0)

    @property
    def agility_required(self) -> int:
        """Number of required agility skill points added to the item"""
        return self._attributes.get("agilityRequirement", 0)

    def __repr__(self) -> str:
        return f"<IngredientComsumableModifiers durability={self.durability}>"
