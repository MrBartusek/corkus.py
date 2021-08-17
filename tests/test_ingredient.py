# pylint: disable=attribute-defined-outside-init

import unittest
from tests import vcr
from corkus import Corkus
from corkus.objects import PartialIngredient, ProfessionType, LogicSymbol
from corkus.errors import BadRequest

class TestIngredient(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.corkus = Corkus()

    @vcr.use_cassette
    async def test_get_ingredient(self):
        glow_bulb = await self.corkus.ingredient.get("Glow Bulb Seeds")
        self.assertEqual(glow_bulb.name, "Glow Bulb Seeds")
        self.assertEqual(glow_bulb.tier, 3)
        self.assertEqual(glow_bulb.required_level, 105)
        self.assertGreater(glow_bulb.sprite.id, 0)
        self.assertIn(ProfessionType.TAILORING, glow_bulb.required_professions)
        self.assertNotEqual(glow_bulb.item_modifiers.durability, 0)
        self.assertGreater(glow_bulb.item_modifiers.defence_required, 0)

        major = await self.corkus.ingredient.get("Major's Badge")
        self.assertNotEqual(major.position_modifiers.above, 0)
        self.assertNotEqual(major.position_modifiers.left, 0)
        self.assertNotEqual(major.position_modifiers.right, 0)
        self.assertNotEqual(major.position_modifiers.under, 0)
        self.assertNotEqual(major.position_modifiers.touching, 0)
        self.assertNotEqual(major.position_modifiers.not_touching, 0)
        self.assertNotEqual(major.consumable_modifiers.duration, 0)

        breath = await self.corkus.ingredient.get("Draconic Bone Marrow")
        self.assertGreater(breath.consumable_modifiers.charges, 0)

        horizon = await self.corkus.ingredient.get("Vortexian Event Horizon")
        self.assertGreater(horizon.sprite.damage, 0)
        self.assertNotEqual(horizon.item_modifiers.durability, 0)
        self.assertGreater(horizon.item_modifiers.strength_required, 0)
        self.assertGreater(horizon.item_modifiers.dexterity_required, 0)
        self.assertGreater(horizon.item_modifiers.intelligence_required, 0)
        self.assertGreater(horizon.item_modifiers.defence_required, 0)
        self.assertGreater(horizon.item_modifiers.agility_required, 0)

    @vcr.use_cassette
    async def test_ingredient_invalid(self):
        with self.assertRaises(BadRequest):
            await self.corkus.ingredient.get('an invalid ingredient')

    @vcr.use_cassette
    async def test_all_ingredient(self):
        all_ingredients = await self.corkus.ingredient.list_all()
        self.assertTrue(any(i.name == "Gaze of Darkness" for i in all_ingredients))

    @vcr.use_cassette
    async def test_search_ingredient_name(self):
        result = await self.corkus.ingredient.search_by_name("Glow Bulb Seeds")
        self.assertEqual(len(result), 1)
        self.assertTrue(result[0].name == "Glow Bulb Seeds")

    @vcr.use_cassette
    async def test_search_ingredient_tier(self):
        result = await self.corkus.ingredient.search_by_tier(2)
        self.assertGreater(len(result), 0)
        self.assertTrue(all(i.tier == 2 for i in result))

    @vcr.use_cassette
    async def test_search_ingredient_level(self):
        result = await self.corkus.ingredient.search_by_level(76)
        self.assertGreater(len(result), 0)
        self.assertTrue(all(i.required_level == 76 for i in result))

    @vcr.use_cassette
    async def test_search_ingredient_professions_and(self):
        result = await self.corkus.ingredient.search_by_professions(
            LogicSymbol.AND,
            [ProfessionType.WOODWORKING, ProfessionType.ALCHEMISM]
        )
        self.assertGreater(len(result), 0)
        for i in result:
            self.assertIn(ProfessionType.WOODWORKING, i.required_professions)
            self.assertIn(ProfessionType.ALCHEMISM, i.required_professions)

    @vcr.use_cassette
    async def test_search_ingredient_professions_or(self):
        result = await self.corkus.ingredient.search_by_professions(
            LogicSymbol.OR,
            [ProfessionType.WOODWORKING, ProfessionType.ALCHEMISM]
        )
        self.assertGreater(len(result), 0)
        for i in result:
            self.assertTrue(
                ProfessionType.WOODWORKING in i.required_professions or
                ProfessionType.ALCHEMISM in i.required_professions
            )

    @vcr.use_cassette
    async def test_partial_ingredient(self):
        ingredient = await PartialIngredient(self.corkus, "Gaze of Darkness").fetch()
        self.assertTrue(ingredient.name == "Gaze of Darkness")

    async def asyncTearDown(self):
        await self.corkus.close()
