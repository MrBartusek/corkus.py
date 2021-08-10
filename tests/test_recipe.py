# pylint: disable=attribute-defined-outside-init

import unittest
from tests import vcr
from corkus import Corkus
from corkus.objects import ItemType, Profession

class TestRecipe(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.corkus = Corkus()

    @vcr.use_cassette
    async def test_get_by_id(self):
        data = [
            # ["ID", "TYPE", "PROFESSION", ""COMBSUMABLE]
            ["Boots-1-3", ItemType.BOOTS, Profession.TAILORING, False],
            ["Bow-1-3", ItemType.BOW, Profession.WOODWORKING, False],
            ["Bracelet-1-3", ItemType.BRACELET, Profession.JEWELING, False],
            ["Chestplate-1-3", ItemType.CHESTPLATE, Profession.ARMOURING, False],
            ["Dagger-1-3", ItemType.DAGGER, Profession.WEAPONSMITHING, False],
            ["Food-1-3", ItemType.FOOD, Profession.COOKING, True],
            ["Helmet-1-3", ItemType.HELMET, Profession.ARMOURING, False],
            ["Necklace-1-3", ItemType.NECKLACE, Profession.JEWELING, False],
            ["Leggings-1-3", ItemType.LEGGINGS, Profession.TAILORING, False],
            ["Potion-1-3", ItemType.POTION, Profession.ALCHEMISM, True],
            ["Relik-1-3", ItemType.RELIK, Profession.WOODWORKING, False],
            ["Ring-1-3", ItemType.RING, Profession.JEWELING, False],
            ["Scroll-1-3", ItemType.SCROLL, Profession.SCRIBING, True],
            ["Spear-1-3", ItemType.SPEAR, Profession.WEAPONSMITHING, False],
            ["Wand-1-3", ItemType.WAND, Profession.WOODWORKING, False]
        ]

        for item in data:
            recipe = await self.corkus.recipe.get_by_id(item[0])
            self.assertEqual(recipe.id, item[0])

            self.assertEqual(recipe.type, item[1])
            self.assertEqual(recipe.skill, item[2])
            if item[3]:
                self.assertIsNone(recipe.durability)
                self.assertEqual(recipe.charges, 3)
                self.assertGreater(recipe.duration.minimum, 0)
                self.assertGreater(recipe.duration.maximum, 0)
            else:
                self.assertIsNone(recipe.charges)
                self.assertIsNone(recipe.duration)
                self.assertGreater(recipe.durability.minimum, 0)
                self.assertGreater(recipe.durability.maximum, 0)

            self.assertEqual(recipe.level.minimum, 1)
            self.assertEqual(recipe.level.maximum, 3)
            self.assertEqual(len(recipe.materials), 2)
            self.assertTrue(recipe.materials[0].name.startswith("Refined "))
            self.assertGreater(recipe.materials[0].amount, 0)
            if item[2] != Profession.JEWELING:
                self.assertGreater(recipe.health_or_damage.minimum, 0)
                self.assertGreater(recipe.health_or_damage.maximum, 0)

    @vcr.use_cassette
    async def test_list_all(self):
        recipes = await self.corkus.recipe.list_all()
        partial_recipe = [r for r in recipes if r.id == "Boots-1-3"][0]
        self.assertEqual(partial_recipe.id, "Boots-1-3")
        self.assertEqual(partial_recipe.type, ItemType.BOOTS)
        self.assertEqual(partial_recipe.level.minimum, 1)
        self.assertEqual(partial_recipe.level.maximum, 3)

        recipe = await partial_recipe.fetch()
        self.assertEqual(recipe.id, "Boots-1-3")

    async def asyncTearDown(self):
        await self.corkus.close()
