# pylint: disable=attribute-defined-outside-init

import unittest
import asyncio
from tests import vcr
from corkus import Corkus
from corkus.objects import ItemType, ItemTier, ClassType, ItemRestrictions, ArmourType
from corkus.errors import InvalidInputError

class TestItem(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        asyncio.get_running_loop().set_debug(False)
        self.corkus = Corkus()

    @vcr.use_cassette
    async def test_get_all(self):
        items = await self.corkus.item.get_all()
        self.assertTrue(all(len(i.name) > 0 for i in items))
        self.assertTrue(any(i.name != i.display_name for i in items))
        self.assertTrue(all(i.set is None or i.set == "Leaf" for i in items))
        self.assertTrue(any(i.required_class == ClassType.ARCHER for i in items))
        self.assertTrue(any(i.required_class == ClassType.WARRIOR for i in items))
        self.assertTrue(any(i.required_class == ClassType.MAGE for i in items))
        self.assertTrue(any(i.required_class == ClassType.ASSASSIN for i in items))
        self.assertTrue(any(i.required_class == ClassType.SKYSEER for i in items))
        self.assertTrue(any(i.restrictions == ItemRestrictions.QUEST_ITEM for i in items))
        self.assertTrue(any(i.restrictions ==  ItemRestrictions.UNTRADABLE for i in items))

        ids = [
            "298:0", "299:0", "300:0", "301:0", "302:0",
            "303:0", "304:0", "305:0", "306:0", "307:0",
            "308:0", "309:0", "310:0", "311:0", "312:0",
            "313:0", "314:0", "315:0", "316:0", "317:0"
        ]
        for id in ids:
            self.assertTrue(any(i.item_id ==  id for i in items))

    @vcr.use_cassette
    async def test_search_wand(self):
        result = await self.corkus.item.search_by_name("Bob's Mythic Wand")
        self.assertEqual(len(result), 1)
        wand = result[0]
        self.assertEqual(wand.type, ItemType.WAND)
        self.assertEqual(wand.tier, ItemTier.LEGENDARY)
        self.assertEqual(wand.sockets, 3)
        self.assertIsNone(wand.armour_type)
        self.assertIsNone(wand.armour_color)
        self.assertEqual(wand.required_level, 75)
        self.assertEqual(wand.required_class, ClassType.MAGE)
        self.assertEqual(wand.required_quest, "Reincarnation")
        self.assertIsNone(wand.lore)
        self.assertIsNone(wand.restrictions)
        self.assertEqual(wand.item_id, "269:19")

    @vcr.use_cassette
    async def test_search_helmet(self):
        result = await self.corkus.item.search_by_name("Scarlet Veil")
        self.assertEqual(len(result), 1)
        helmet = result[0]
        self.assertEqual(helmet.type, ItemType.HELMET)
        self.assertEqual(helmet.tier, ItemTier.FABLED)
        self.assertEqual(helmet.sockets, 0)
        self.assertEqual(helmet.armour_type, ArmourType.CHAIN)
        self.assertIsNone(helmet.armour_color)
        self.assertEqual(helmet.required_level, 52)
        self.assertIsNone(helmet.required_class)
        self.assertIsNone(helmet.required_quest, "Reincarnation")
        self.assertEqual(helmet.lore, "You're seeing red... Time to see more of it.")
        self.assertIsNone(helmet.restrictions)
        self.assertEqual(helmet.item_id, "302:0")

    @vcr.use_cassette
    async def test_search_chestplate(self):
        result = await self.corkus.item.search_by_name("Snail Mail")
        self.assertEqual(len(result), 1)
        chestplate = result[0]
        self.assertEqual(chestplate.type, ItemType.CHESTPLATE)
        self.assertEqual(chestplate.tier, ItemTier.SET)
        self.assertEqual(chestplate.sockets, 3)
        self.assertEqual(chestplate.armour_type, ArmourType.LEATHER)
        self.assertEqual(chestplate.armour_color.r, 0)
        self.assertEqual(chestplate.armour_color.g, 51)
        self.assertEqual(chestplate.armour_color.b, 51)
        self.assertEqual(chestplate.armour_color.hex, "#003333")
        self.assertEqual(chestplate.required_level, 97)
        self.assertIsNone(chestplate.required_class)
        self.assertIsNone(chestplate.required_quest)
        self.assertIsNone(chestplate.lore)
        self.assertIsNone(chestplate.restrictions)
        self.assertEqual(chestplate.item_id, "299:0")

    @vcr.use_cassette
    async def test_search_type_invalid(self):
        with self.assertRaises(InvalidInputError):
            await self.corkus.item.search_by_type(ItemType.POTION)

    @vcr.use_cassette
    async def test_search_type(self):
        items = await self.corkus.item.search_by_type(ItemType.NECKLACE)
        self.assertTrue(all(i.type == ItemType.NECKLACE for i in items))

    async def asyncTearDown(self):
        await self.corkus.close()
