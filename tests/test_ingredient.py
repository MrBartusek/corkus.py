# pylint: disable=attribute-defined-outside-init

import unittest
from tests import vcr
from corkus import Corkus
from corkus.objects import PartialIngredient

class TestIngredient(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.corkus = Corkus()

    @vcr.use_cassette
    async def test_get_ingredient(self):
        ingredient = await self.corkus.ingredient.get("Gaze of Darkness")
        self.assertEqual(ingredient.name, "Gaze of Darkness")
        self.assertEqual(ingredient.tier, 3)
        self.assertEqual(ingredient.reqired_level, 105)

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
