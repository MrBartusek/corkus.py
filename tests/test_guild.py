# pylint: disable=attribute-defined-outside-init

import unittest
from corkus import Corkus
from corkus.objects import PartialGuild

class TestGuild(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.corkus = Corkus()

    async def test_get_guild(self):
        guild = await self.corkus.guild.get("The Farplane")
        self.assertEqual(guild.name, "The Farplane")
        self.assertEqual(guild.tag, "Yin")
        self.assertGreater(sum([m.contributed_xp for m in guild.members]), 0)
        self.assertTrue(all([m.join_date < m.guild.created for m in guild.members]))
        self.assertTrue(0 <= guild.level_progress <= 100)
        self.assertTrue(1 <= guild.level <= 100)
        member = guild.members[0]
        player = await member.fetch_player()
        self.assertEqual(player.guild.name, "The Farplane")

    async def test_all_guilds(self):
        all_guilds = await self.corkus.guild.list_all()
        self.assertTrue(any([g.name == "The Farplane" for g in all_guilds]))

    async def test_partial_guild(self):
        guild = await PartialGuild(self.corkus, "The Farplane").fetch()
        self.assertTrue(guild.tag == "Yin")

    async def test_partial_member_fetch(self):
        player = await self.corkus.player.get('MrBartusekXD')
        self.assertEqual(player.guild.name, "The Farplane")
        member = await player.member.fetch()
        self.assertEqual(member.guild.name, "The Farplane")

    async def asyncTearDown(self):
        await self.corkus.close()
