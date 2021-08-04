# pylint: disable=attribute-defined-outside-init

import unittest
from tests import vcr
from corkus import Corkus
from corkus.objects import CorkusUUID, PartialPlayer, PlayerTag, HardcoreType, ClassType

class TestPlayer(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.corkus = Corkus()

    @vcr.use_cassette
    async def test_player_get_uuid(self):
        uuid = await self.corkus.player.get_uuid('MrBartusekXD')
        self.assertEqual(uuid, CorkusUUID('0edc3eb6-74d8-49b6-8b2a-3c0782183e3a'))

    @vcr.use_cassette
    async def test_player_get_stats_uuid(self):
        player = await self.corkus.player.get(CorkusUUID('0edc3eb6-74d8-49b6-8b2a-3c0782183e3a'))
        self.assertEqual(player.username, "MrBartusekXD")

    @vcr.use_cassette
    async def test_fetch_partial(self):
        partial = PartialPlayer(self.corkus, username = "MrBartusekXD")
        player = await partial.fetch()
        self.assertEqual(player.uuid, CorkusUUID('0edc3eb6-74d8-49b6-8b2a-3c0782183e3a'))

    @vcr.use_cassette
    async def test_player_general(self):
        player = await self.corkus.player.get('MrBartusekXD')

        self.assertEqual(player.uuid, CorkusUUID('0edc3eb6-74d8-49b6-8b2a-3c0782183e3a'))

        # Overall
        self.assertGreater(player.playtime.raw, 0)
        self.assertEqual(player.tag, PlayerTag.VIP)

        # Guild
        self.assertEqual(player.member.username, "MrBartusekXD")
        self.assertEqual(player.guild.name, "The Farplane")

        # Stats
        self.assertGreater(player.statistics.chests_found, 0)
        self.assertGreater(player.statistics.blocksWalked, 0)
        self.assertGreater(player.statistics.mobs_killed, 0)
        self.assertGreater(player.statistics.total_combat_level, 0)
        self.assertGreater(player.statistics.total_profession_level, 0)
        self.assertGreater(player.statistics.logins, 0)
        self.assertGreater(player.statistics.deaths, 0)
        self.assertGreater(player.statistics.discoveries, 0)

        # Classes
        player_class = player.classes[0]
        self.assertGreater(player_class.statistics.chests_found, 0)
        self.assertFalse(player_class.gamemode.craftsman)
        self.assertFalse(player_class.gamemode.hunted)
        self.assertFalse(player_class.gamemode.ironman)
        self.assertEqual(player_class.gamemode.hardcore, HardcoreType.DISABLED)
        self.assertGreater(player_class.statistics.deaths, 0)
        self.assertGreater(player_class.statistics.discoveries, 0)
        self.assertGreater(player_class.statistics.logins, 0)
        self.assertTrue(any(q.name == "King's Recruit" for q in player_class.quests))
        self.assertTrue(any(q.wiki_url == "https://wynncraft.fandom.com/wiki/King's_Recruit" for q in player_class.quests))
        self.assertTrue(any(q.wiki_url == "https://wynncraft.fandom.com/wiki/Quests#Mini-Quests" for q in player_class.quests))
        self.assertEqual(player_class.type, ClassType.MAGE)
        self.assertEqual(player_class.type, ClassType.MAGE)
        self.assertEqual(player_class.name, "mage")
        self.assertEqual(player_class.display_name, "Mage")

    async def asyncTearDown(self):
        await self.corkus.close()
