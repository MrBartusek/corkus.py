# pylint: disable=attribute-defined-outside-init

import unittest
from tests import vcr
import time
from corkus import Corkus
from corkus.objects import (
    CorkusUUID,
    PartialPlayer,
    PlayerTag,
    HardcoreType,
    ClassType,
    PartialServer,
    ServerType,
    ProfessionType,
    DungeonType,
    GuildRank
)
from corkus.errors import BadRequest

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
    async def test_player_empty_partial(self):
        with self.assertRaises(ValueError):
            PartialPlayer(self.corkus)

    @vcr.use_cassette
    async def test_player_invalid(self):
        with self.assertRaises(BadRequest) as e:
            await self.corkus.player.get('an invalid username')
        self.assertEqual(e.exception.response.status, 400)

    @vcr.use_cassette
    async def test_player_partial(self):
        partial = PartialPlayer(self.corkus, uuid = CorkusUUID('0edc3eb6-74d8-49b6-8b2a-3c0782183e3a'))
        self.assertEqual(partial.uuid, CorkusUUID('0edc3eb6-74d8-49b6-8b2a-3c0782183e3a'))
        player = await partial.fetch()
        self.assertEqual(player.username, "MrBartusekXD")

    @vcr.use_cassette
    # pylint: disable=too-many-statements
    async def test_player_general(self):
        player = await self.corkus.player.get('MrBartusekXD')

        self.assertEqual(player.uuid, CorkusUUID('0edc3eb6-74d8-49b6-8b2a-3c0782183e3a'))

        # Overall
        self.assertGreater(player.playtime.raw, 0)
        self.assertEqual(player.tag, PlayerTag.VIP)
        self.assertEqual(player.join_date.year, 2020)

        # Combined from classes
        self.assertTrue(all(d.completed > 0 for d in player.dungeons))
        self.assertEqual(player.dungeons[0].name, "Decrepit Sewers")
        self.assertTrue(any(q.name == "King's Recruit" for q in player.quests))

        # Guild
        self.assertEqual(player.member.username, "MrBartusekXD")
        self.assertEqual(player.member.rank, GuildRank.CHIEF)
        self.assertEqual(player.guild.name, "The Farplane")
        self.assertEqual(player.member.guild.name, "The Farplane")
        self.assertEqual(player.member.player.username, "MrBartusekXD")

        # Status
        self.assertFalse(player.status.online)
        self.assertIsNone(player.status.server)
        diff = abs(int(player.last_online.timestamp()) - int(time.time()))
        self.assertGreater(diff, 600)

        # Stats
        self.assertGreater(player.statistics.chests_found, 0)
        self.assertGreater(player.statistics.blocks_walked, 0)
        self.assertGreater(player.statistics.mobs_killed, 0)
        self.assertGreater(player.statistics.total_combat_level, 0)
        self.assertGreater(player.statistics.total_profession_level, 0)
        self.assertGreater(player.statistics.logins, 0)
        self.assertGreater(player.statistics.deaths, 0)
        self.assertGreater(player.statistics.discoveries, 0)
        self.assertEqual(player.statistics.items_identified, 0)

        # Classes
        player_class = player.classes[0]
        self.assertGreater(player_class.statistics.chests_found, 0)
        self.assertFalse(player_class.gamemode.craftsman)
        self.assertFalse(player_class.gamemode.hunted)
        self.assertFalse(player_class.gamemode.ironman)
        self.assertEqual(player_class.gamemode.hardcore, HardcoreType.DISABLED)
        self.assertTrue(player_class.approximate_create[0] <= player.join_date <= (player_class.approximate_create[1]))

        # Classes - Statistics
        self.assertGreater(player_class.statistics.deaths, 0)
        self.assertGreater(player_class.statistics.discoveries, 0)
        self.assertGreater(player_class.statistics.logins, 0)

        # Classes - Quests
        self.assertTrue(any(q.name == "King's Recruit" for q in player_class.quests))
        self.assertTrue(any(q.wiki_url == "https://wynncraft.fandom.com/wiki/King's_Recruit" for q in player_class.quests))
        self.assertTrue(any(q.wiki_url == "https://wynncraft.fandom.com/wiki/Quests#Mini-Quests" for q in player_class.quests))

        # Classes - Type
        self.assertEqual(player_class.type, ClassType.MAGE)
        self.assertEqual(player_class.kind, ClassType.MAGE)
        self.assertEqual(player_class.name, "mage")
        self.assertEqual(player_class.display_name, "Mage")

        # Classes - Dungeons
        self.assertTrue(all(d.completed > 0 for d in player_class.dungeons))
        self.assertEqual(player_class.dungeons[0].name, "Decrepit Sewers")
        self.assertEqual(player_class.dungeons[0].type, DungeonType.STANDARD)

        # Classes - Professions
        self.assertEqual(len(player_class.professions), 13)
        self.assertTrue(all(p.level > 10 for p in player_class.professions))
        self.assertEqual(player_class.combat.type, ProfessionType.COMBAT)
        self.assertEqual(player_class.combat.name, "Combat")
        self.assertEqual(player_class.get_profession(ProfessionType.ALCHEMISM).type, ProfessionType.ALCHEMISM)
        self.assertGreater(player_class.combat.level_progress, 0)

        # Alternative player
        player = await self.corkus.player.get("ojomFox")
        player_class = player.classes[0]
        self.assertTrue(all(r.completed > 0 for r in player_class.raids))
        self.assertEqual(player.raids[0].name, "The Canyon Colossus")
        self.assertEqual(player_class.raids[0].name, "The Canyon Colossus")
        self.assertTrue(any(d.type == DungeonType.STANDARD for d in player_class.dungeons))
        self.assertTrue(any(d.type == DungeonType.CORRUPTED for d in player_class.dungeons))
        self.assertTrue(any(d.type == DungeonType.REMOVED for d in player_class.dungeons))

    @vcr.use_cassette
    async def test_player_no_guild(self):
        player = await self.corkus.player.get("Salted")
        self.assertIsNone(player.guild)
        self.assertIsNone(player.member)

    @vcr.use_cassette
    async def test_player_partial_server(self):
        partial_server = PartialServer(self.corkus, "WC1")
        self.assertEqual(partial_server.name, "WC1")
        self.assertEqual(partial_server.type, ServerType.STANDARD)

        server = await partial_server.fetch()
        self.assertEqual(server.name, "WC1")

    @vcr.use_cassette
    async def test_player_partial_server_invalid(self):
        partial_server = PartialServer(self.corkus, "invalid")
        server = await partial_server.fetch()
        self.assertEqual(server, None)

    async def asyncTearDown(self):
        await self.corkus.close()
