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

    async def test_all_guilds(self):
        all_guilds = await self.corkus.guild.list_all()
        self.assertTrue(any([g.name == "The Farplane" for g in all_guilds]))

    async def test_partial_guild(self):
        guild = await PartialGuild(self.corkus, "The Farplane").fetch()
        self.assertTrue(guild.tag == "Yin")

    async def asyncTearDown(self):
        await self.corkus.close()
