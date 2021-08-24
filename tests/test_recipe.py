# pylint: disable=attribute-defined-outside-init

import unittest
from tests import vcr
from corkus import Corkus
from corkus.objects import ItemType, ProfessionType, ItemCategory

class TestRecipe(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.corkus = Corkus()

    @vcr.use_cassette
    async def test_recipe_get_by_id(self):
        items = [
            # ["ID", "TYPE", "PROFESSION", ""COMBSUMABLE]
            ["Boots-1-3", ItemType.BOOTS, ProfessionType.TAILORING, ItemCategory.ARMOUR],
            ["Bow-1-3", ItemType.BOW, ProfessionType.WOODWORKING, ItemCategory.WEAPON],
            ["Bracelet-1-3", ItemType.BRACELET, ProfessionType.JEWELING, ItemCategory.ACCESSORY],
            ["Chestplate-1-3", ItemType.CHESTPLATE, ProfessionType.ARMOURING, ItemCategory.ARMOUR],
            ["Dagger-1-3", ItemType.DAGGER, ProfessionType.WEAPONSMITHING, ItemCategory.WEAPON],
            ["Food-1-3", ItemType.FOOD, ProfessionType.COOKING, ItemCategory.COMSUMABLE],
            ["Helmet-1-3", ItemType.HELMET, ProfessionType.ARMOURING, ItemCategory.ARMOUR],
            ["Necklace-1-3", ItemType.NECKLACE, ProfessionType.JEWELING, ItemCategory.ACCESSORY],
            ["Leggings-1-3", ItemType.LEGGINGS, ProfessionType.TAILORING, ItemCategory.ARMOUR],
            ["Potion-1-3", ItemType.POTION, ProfessionType.ALCHEMISM, ItemCategory.COMSUMABLE],
            ["Relik-1-3", ItemType.RELIK, ProfessionType.WOODWORKING, ItemCategory.WEAPON],
            ["Ring-1-3", ItemType.RING, ProfessionType.JEWELING, ItemCategory.ACCESSORY],
            ["Scroll-1-3", ItemType.SCROLL, ProfessionType.SCRIBING, ItemCategory.COMSUMABLE],
            ["Spear-1-3", ItemType.SPEAR, ProfessionType.WEAPONSMITHING, ItemCategory.WEAPON],
            ["Wand-1-3", ItemType.WAND, ProfessionType.WOODWORKING, ItemCategory.WEAPON]
        ]

        for item in items:
            recipe = await self.corkus.recipe.get_by_id(item[0])
            self.assertEqual(recipe.id, item[0])

            self.assertEqual(recipe.type, item[1])
            self.assertEqual(recipe.profession, item[2])
            self.assertEqual(recipe.category, item[3])
            if item[3] == ItemCategory.COMSUMABLE:
                self.assertIsNone(recipe.durability)
                self.assertEqual(recipe.charges, 3)
                self.assertGreater(recipe.duration.min, 0)
                self.assertGreater(recipe.duration.max, 0)
            else:
                self.assertIsNone(recipe.charges)
                self.assertIsNone(recipe.duration)
                self.assertGreater(recipe.durability.min, 0)
                self.assertGreater(recipe.durability.max, 0)

            self.assertEqual(recipe.level.min, 1)
            self.assertEqual(recipe.level.max, 3)
            self.assertEqual(len(recipe.materials), 2)
            self.assertTrue(recipe.materials[0].name.startswith("Refined "))
            self.assertGreater(recipe.materials[0].amount, 0)
            if item[2] != ProfessionType.JEWELING:
                self.assertGreater(recipe.health_or_damage.min, 0)
                self.assertGreater(recipe.health_or_damage.max, 0)

    @vcr.use_cassette
    async def test_recipe_all(self):
        recipes = await self.corkus.recipe.list_all()
        partial_recipe = [r for r in recipes if r.id == "Boots-1-3"][0]
        self.assertEqual(partial_recipe.id, "Boots-1-3")
        self.assertEqual(partial_recipe.type, ItemType.BOOTS)
        self.assertEqual(partial_recipe.level.min, 1)
        self.assertEqual(partial_recipe.level.max, 3)

        recipe = await partial_recipe.fetch()
        self.assertEqual(recipe.id, "Boots-1-3")

    @vcr.use_cassette
    async def test_recipe_search_type(self):
        result = await self.corkus.recipe.search_by_type(ItemType.HELMET)
        self.assertGreater(len(result), 0)
        self.assertTrue(all(r.type == ItemType.HELMET for r in result))

    @vcr.use_cassette
    async def test_recipe_search_profession(self):
        result = await self.corkus.recipe.search_by_profession(ProfessionType.WOODWORKING)
        self.assertGreater(len(result), 0)
        self.assertTrue(all(r.profession == ProfessionType.WOODWORKING for r in result))

    async def asyncTearDown(self):
        await self.corkus.close()
