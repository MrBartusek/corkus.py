from __future__ import annotations
from .base import CorkusBase
from .skill_points import SkillPoints

class IngredientItemModifiers(CorkusBase):
    """Modifier of :py:class:`Ingredient` applied to regular crafted items."""
    @property
    def durability(self) -> int:
        """Modifier on item durability."""
        return self._attributes.get("durabilityModifier", 0)

    @property
    def skill_points(self) -> SkillPoints:
        """Number of required skill points added to the item."""
        return SkillPoints(
            corkus = self._corkus,
            strength = self._attributes.get("strengthRequirement", 0),
            dexterity = self._attributes.get("dexterityRequirement", 0),
            intelligence = self._attributes.get("intelligenceRequirement", 0),
            defence = self._attributes.get("defenceRequirement", 0),
            agility = self._attributes.get("agilityRequirement", 0)
        )

    def __repr__(self) -> str:
        return f"<IngredientComsumableModifiers durability={self.durability} skill_points={self.skill_points}>"
