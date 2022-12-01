# pylint: disable=attribute-defined-outside-init

import unittest
import asyncio
from tests import vcr
from corkus import Corkus
from corkus.objects import (
    ItemType,
    ItemTier,
    CharacterType,
    ItemRestrictions,
    ArmourType,
    ItemCategory,
    AttackSpeed,
    IdentificationType
)
from corkus.errors import InvalidInputError

class TestItem(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        asyncio.get_running_loop().set_debug(False)
        self.corkus = Corkus()
        await self.corkus.start()

    @vcr.use_cassette
    async def test_item_all(self):
        items = await self.corkus.item.get_all()
        self.assertTrue(all(len(i.name) > 0 for i in items))
        self.assertTrue(any(i.name != i.display_name for i in items))
        self.assertTrue(all(i.set is None or i.set == "Leaf" for i in items))
        self.assertTrue(any(i.required_class == CharacterType.ARCHER for i in items))
        self.assertTrue(any(i.required_class == CharacterType.WARRIOR for i in items))
        self.assertTrue(any(i.required_class == CharacterType.MAGE for i in items))
        self.assertTrue(any(i.required_class == CharacterType.ASSASSIN for i in items))
        self.assertTrue(any(i.required_class == CharacterType.SKYSEER for i in items))
        self.assertTrue(any(i.restrictions == ItemRestrictions.QUEST_ITEM for i in items))
        self.assertTrue(any(i.restrictions ==  ItemRestrictions.UNTRADABLE for i in items))

        self.assertTrue(any(i.type == ItemType.HELMET for i in items))
        self.assertTrue(any(i.type == ItemType.CHESTPLATE for i in items))
        self.assertTrue(any(i.type == ItemType.LEGGINGS for i in items))
        self.assertTrue(any(i.type == ItemType.BOOTS for i in items))
        self.assertTrue(any(i.type == ItemType.RING for i in items))
        self.assertTrue(any(i.type == ItemType.NECKLACE for i in items))
        self.assertTrue(any(i.type == ItemType.BRACELET for i in items))
        self.assertTrue(any(i.type == ItemType.DAGGER for i in items))
        self.assertTrue(any(i.type == ItemType.SPEAR for i in items))
        self.assertTrue(any(i.type == ItemType.BOW for i in items))
        self.assertTrue(any(i.type == ItemType.WAND for i in items))
        self.assertTrue(any(i.type == ItemType.RELIK for i in items))

        self.assertTrue(any(i.category == ItemCategory.ACCESSORY for i in items))
        self.assertTrue(any(i.category == ItemCategory.WEAPON for i in items))
        self.assertFalse(any(i.category == ItemCategory.COMSUMABLE for i in items))
        self.assertTrue(any(i.category == ItemCategory.ARMOUR for i in items))

        ids = [
            "298:0", "299:0", "300:0", "301:0", "302:0",
            "303:0", "304:0", "305:0", "306:0", "307:0",
            "308:0", "309:0", "310:0", "311:0", "312:0",
            "313:0", "314:0", "315:0", "316:0", "317:0"
        ]
        for id in ids:
            self.assertTrue(any(i.item_id ==  id for i in items))

    @vcr.use_cassette
    async def test_item_search_wand(self):
        result = await self.corkus.item.search_by_name("Bob's Mythic Wand")
        self.assertEqual(len(result), 1)
        wand = result[0]
        self.assertEqual(wand.type, ItemType.WAND)
        self.assertEqual(wand.tier, ItemTier.LEGENDARY)
        self.assertEqual(wand.sockets, 3)
        self.assertIsNone(wand.armour_type)
        self.assertIsNone(wand.armour_color)
        self.assertEqual(wand.required_level, 75)
        self.assertEqual(wand.required_class, CharacterType.MAGE)
        self.assertEqual(wand.required_quest, "Reincarnation")
        self.assertIsNone(wand.lore)
        self.assertIsNone(wand.restrictions)
        self.assertEqual(wand.item_id, "269:19")
        self.assertEqual(wand.category, ItemCategory.WEAPON)
        self.assertIsNone(wand.armour_type)
        self.assertEqual(wand.damage.neutral, "125-180")
        self.assertEqual(wand.attack_speed, AttackSpeed.NORMAL)
        self.assertTrue(wand.identified)
        self.assertIsNone(wand.health)
        self.assertIsNone(wand.armour_defence)
        self.assertIsNone(wand.skin)
        self.assertTrue(any(i.type == IdentificationType.LOOT_BONUS and i.value > 0 and i.values is None for i in wand.identifications))

    @vcr.use_cassette
    async def test_item_search_helmet(self):
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
        self.assertIsNone(helmet.skin)
        self.assertIsNone(helmet.damage)
        self.assertIsNone(helmet.attack_speed)

        self.assertTrue(any(i.type == IdentificationType.EARTH_DEFENSE and i.value == -30 for i in helmet.identifications))
        self.assertTrue(any(i.type == IdentificationType.WALK_SPEED and i.values.min == 2 and i.values.max == 10 for i in helmet.identifications))

        self.assertEqual(len(helmet.major_identifications), 1)
        identification = helmet.major_identifications[0]
        self.assertEqual(identification.name, "Explosive Impact")
        self.assertEqual(identification.effect, 'Your "Exploding" ID can trigger whet hitting mobs with your basic attack')
        self.assertEqual(identification.id, "EXPLOSIVE_IMPACT")

    @vcr.use_cassette
    async def test_item_search_chestplate(self):
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
        self.assertIsNone(chestplate.skin)
        self.assertGreater(chestplate.skill_points.strength, 0)

    @vcr.use_cassette
    async def test_item_search_head(self):
        result = await self.corkus.item.search_by_name("Happy Gert Mask")
        self.assertEqual(len(result), 1)
        mask = result[0]
        self.assertGreater(mask.health, 0)
        self.assertGreater(mask.armour_defence.earth, 0)
        self.assertLess(mask.armour_defence.fire, 0)
        self.assertGreater(mask.required_level, 0)
        self.assertEqual(mask.item_id, "397:3")
        self.assertIsNone(mask.armour_type)
        self.assertEqual(mask.skin.username, "catsinspacee")
        self.assertGreater(mask.skin.requested.timestamp(), 1000)
        self.assertIsNotNone(mask.skin.uuid)
        self.assertTrue(mask.skin.url.startswith("http://textures.minecraft.net/texture/"))

    @vcr.use_cassette
    async def test_item_search_type_invalid(self):
        with self.assertRaises(InvalidInputError):
            await self.corkus.item.search_by_type(ItemType.POTION)

    @vcr.use_cassette
    async def test_item_search_type(self):
        items = await self.corkus.item.search_by_type(ItemType.NECKLACE)
        self.assertTrue(all(i.type == ItemType.NECKLACE for i in items))

    async def asyncTearDown(self):
        await self.corkus.close()
