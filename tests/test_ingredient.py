# pylint: disable=attribute-defined-outside-init

import unittest
from tests import vcr
from corkus import Corkus
from corkus.objects import PartialIngredient, ProfessionType
from corkus.errors import BadRequest

class TestIngredient(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.corkus = Corkus()

    @vcr.use_cassette
    async def test_get_ingredient(self):
        glow_bulb = await self.corkus.ingredient.get("Glow Bulb Seeds")
        self.assertEqual(glow_bulb.name, "Glow Bulb Seeds")
        self.assertEqual(glow_bulb.tier, 3)
        self.assertEqual(glow_bulb.reqired_level, 105)
        self.assertGreater(glow_bulb.sprite.id, 0)
        self.assertIn(ProfessionType.TAILORING, glow_bulb.reqired_professions)
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
        with self.assertRaises(BadRequest) as e:
            await self.corkus.ingredient.get('an invalid ingredient')

    @vcr.use_cassette
    async def test_all_ingredient(self):
        all_ingredients = await self.corkus.ingredient.list_all()
        self.assertTrue(any(i.name == "Gaze of Darkness" for i in all_ingredients))

    @vcr.use_cassette
    async def test_partial_ingredient(self):
        ingredient = await PartialIngredient(self.corkus, "Gaze of Darkness").fetch()
        self.assertTrue(ingredient.name == "Gaze of Darkness")

    async def asyncTearDown(self):
        await self.corkus.close()
