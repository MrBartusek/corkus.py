# pylint: disable=attribute-defined-outside-init

from typing import List
from corkus.objects import LeaderboardPlayer
import unittest
from corkus import Corkus
from tests import vcr

class TestLeaderboard(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.corkus = Corkus()

    @vcr.use_cassette
    async def test_leaderboard_guild(self):
        result = await self.corkus.leaderboard.guild()
        for guild in result:
            self.assertGreater(len(guild.name), 0)
            self.assertGreater(len(guild.tag), 0)
            self.assertGreater(guild.total_xp, 0)
            self.assertGreater(guild.level, 1)
            self.assertGreater(guild.members_count, 0)
            self.assertTrue(1 <= guild.position <= 100)

        self.assertTrue(any(g.war_count > 0 for g in result))

        guild = await [g for g in result if g.name == "Avicia"][0].fetch()
        self.assertEqual(guild.name, "Avicia")

    @vcr.use_cassette
    async def test_leaderboard_combat(self):
        result = await self.corkus.leaderboard.combat()
        await self.check_players(result)

    @vcr.use_cassette
    async def test_leaderboard_pvp(self):
        result = await self.corkus.leaderboard.pvp()
        await self.check_players(result)

    async def check_players(self, result: List[LeaderboardPlayer]):
        guild_count = 0
        for player in result:
            self.assertGreater(len(player.username), 0)
            self.assertGreater(player.total_combat_level, 0)
            self.assertGreater(player.playtime.raw, 0)
            self.assertGreater(player.total_xp, 0)
            self.assertGreater(player.position, 0)
            if player.guild:
                guild_count += 1
                self.assertGreater(len(player.guild.name), 0)
                self.assertGreater(len(player.member.tag), 0)
            else:
                self.assertIsNone(player.member)

        self.assertTrue(any(p.pvp_kills > 0 for p in result))

        self.assertGreater(guild_count, 0)
        self.assertLess(guild_count, len(result))

        player = await [p for p in result if p.username == "Maarcus1"][0].fetch()
        self.assertEqual(player.username, "Maarcus1")

    async def asyncTearDown(self):
        await self.corkus.close()
