from __future__ import annotations
from typing import Union
from enum import Enum

class IdentificationType(Enum):
    # Additional skill points
    AGILITY_POINTS = "AGILITY_POINTS"
    """Additional agility points granted by this item."""
    DEFENSE_POINTS = "DEFENSE_POINTS"
    """Additional defence points granted by this item."""
    DEXTERITY_POINTS = "DEXTERITY_POINTS"
    """Additional dexterity points granted by this item."""
    INTELLIGENCE_POINTS = "INTELLIGENCE_POINTS"
    """Additional intelligence points granted by this item."""
    STRENGTH_POINTS = "STRENGTH_POINTS"
    """Additional strength points granted by this item."""

    # Attack
    ATTACK_SPEED = "ATTACK_SPEED"
    """Tier modifier to attack speed."""
    DAMAGE_BONUS = "DAMAGE_BONUS"
    """Percentage melee damage modifier."""
    DAMAGE_BONUS_RAW = "DAMAGE_BONUS_RAW"
    """Bonus to melee damage."""
    SPELL_DAMAGE = "SPELL_DAMAGE"
    """Percentage spell damage modifier."""
    SPELL_DAMAGE_RAW = "SPELL_DAMAGE_RAW"
    """Bonus to spell damage."""

    # Spells
    RAINBOW_SPELL_DAMAGE_RAW = "RAINBOW_SPELL_DAMAGE_RAW"
    """Bonus to rainbow spell damage."""
    SPELL_COST_1 = "SPELL_COST_1"
    """Modifier on cost of 1st spell."""
    SPELL_COST_1_RAW = "SPELL_COST_1_RAW"
    """Precentage modifier on cost of 1st spell."""
    SPELL_COST_2 = "SPELL_COST_2"
    """Modifier on cost of 2nd spell."""
    SPELL_COST_2_RAW = "SPELL_COST_2_RAW"
    """Precentage modifier on cost of 2nd spell."""
    SPELL_COST_3 = "SPELL_COST_3"
    """Modifier on cost of 3rd spell."""
    SPELL_COST_3_RAW = "SPELL_COST_3_RAW"
    """Precentage modifier on cost of 3rd spell."""
    SPELL_COST_4 = "SPELL_COST_4"
    """Modifier on cost of 4th spell."""
    SPELL_COST_4_RAW = "SPELL_COST_4_RAW"
    """Precentage modifier on cost of 4th spell."""

    # Elemental damage
    AIR_DAMAGE_BONUS = "AIR_DAMAGE_BONUS"
    """Percentage bonus to air damage."""
    EARTH_DAMAGE_BONUS = "EARTH_DAMAGE_BONUS"
    """Percentage bonus to earth damage."""
    FIRE_DAMAGE_BONUS = "FIRE_DAMAGE_BONUS"
    """Percentage bonus to fire damage."""
    THUNDER_DAMAGE_BONUS = "THUNDER_DAMAGE_BONUS"
    """Percentage bonus to thunder damage."""
    WATER_DAMAGE_BONUS = "WATER_DAMAGE_BONUS"
    """Percentage bonus to water damage."""

    # Elemental defence
    AIR_DEFENSE = "AIR_DEFENSE"
    """Air defense points granted by this item."""
    EARTH_DEFENSE = "EARTH_DEFENSE"
    """Earth defense points granted by this item."""
    FIRE_DEFENSE = "FIRE_DEFENSE"
    """Fire defense points granted by this item."""
    THUNDER_DEFENSE = "THUNDER_DEFENSE"
    """Thunder defense points granted by this item."""
    WATER_DEFENSE = "WATER_DEFENSE"
    """Wather defense points granted by this item."""

    AIR_DEFENSE_BONUS = "AIR_DEFENSE_BONUS"
    """Percentage bonus to air defense."""
    EARTH_DEFENSE_BONUS = "EARTH_DEFENSE_BONUS"
    """Percentage bonus to earth defense."""
    FIRE_DEFENSE_BONUS = "FIRE_DEFENSE_BONUS"
    """Percentage bonus to fire defense."""
    THUNDER_DEFENSE_BONUS = "THUNDER_DEFENSE_BONUS"
    """Percentage bonus to thunder defense."""
    WATER_DEFENSE_BONUS = "WATER_DEFENSE_BONUS"
    """Percentage bonus to wather defense."""

    # Health and mana
    HEALTH_BONUS = "HEALTH_BONUS"
    """Health modifier."""
    HEALTH_REGEN = "HEALTH_REGEN"
    """Percentage health regeneration modifier."""
    HEALTH_REGEN_RAW = "HEALTH_REGEN_RAW"
    """Bonus to health regeneration."""
    LIFE_STEAL = "LIFE_STEAL"
    """Amount of health stolen from enemy per attack across next 4 seconds."""
    MANA_STEAL = "MANA_STEAL"
    """Amount of mana stolen from enemy per attack across next 4 seconds."""
    MANA_REGEN = "MANA_REGEN"
    """Mana regeneration bonus per 4 seconds."""

    # Passive damage
    POISON = "POISON"
    """Percentage poison modifier."""
    REFLECTION = "REFLECTION"
    """Percentage reflection modifier."""
    THORNS = "THORNS"
    """Percentage thorns modifier."""
    EXPLODING = "EXPLODING"
    """Percentage exploding modifier."""

    # Movement
    WALK_SPEED = "WALK_SPEED"
    """Percentage walk speed modifier"""
    SPRINT = "SPRINT"
    """Percentage modifier on rate of depleting sprint bar."""
    SPRINT_REGEN = "SPRINT_REGEN"
    """Percentage sprint regeneration modifier"""
    JUMP_HEIGHT = "JUMP_HEIGHT"
    """Jump height modifier"""

    LOOT_BONUS = "LOOT_BONUS"
    """Percentage loot bonus modifier."""
    LOOT_QUALITY = "LOOT_QUALITY"
    """Percentage loot quality modifier."""
    XP_BONUS = "XP_BONUS"
    """Percentage XP bonus modifier."""
    EMERALD_STEALING = "EMERALD_STEALING"
    """Percentage bonus chance to steal an emerald on hit."""
    GATHER_XP_BONUS = "GATHER_XP_BONUS"
    """Percentage of additional XP when gartering."""
    GATHER_SPEED = "GATHER_SPEED"
    """Percentage modifier to gartering speed."""
    SOUL_POINTS = "SOUL_POINTS"
    """Percentage chance to regenerate an additional soul point."""

    @staticmethod
    def from_items_api(key: str) -> Union[IdentificationType, None]:
        from corkus.data import ids_convert
        return next((id["type"] for id in ids_convert if id["items_api"] == key), None)

    @staticmethod
    def from_ingredient_api(key: str) -> Union[IdentificationType, None]:
        from corkus.data import ids_convert
        return next((id["type"] for id in ids_convert if id["ingredient_api"] == key), None)

    @staticmethod
    def to_items_api(type: IdentificationType) -> str:
        from corkus.data import ids_convert
        return next((id["items_api"] for id in ids_convert if id["type"] == type), None)

    @staticmethod
    def to_ingredient_api(type: IdentificationType) -> str:
        from corkus.data import ids_convert
        return next((id["ingredient_api"] for id in ids_convert if id["type"] == type), None)
