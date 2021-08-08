# pylint: disable=attribute-defined-outside-init

import unittest
from corkus import Corkus
from tests import vcr

class TestSearch(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.corkus = Corkus()

    @vcr.use_cassette
    async def test_guilds_and_players(self):
        result = await self.corkus.search.guilds_and_players("MrBartusekXD")
        self.assertEqual(result.term, "mrbartusekxd")
        self.assertTrue(any(p.username == "MrBartusekXD" for p in result.players))

        result = await self.corkus.search.guilds_and_players("farplane")
        self.assertTrue(any(g.name == "The Farplane" for g in result.guilds))

    @vcr.use_cassette
    async def test_players(self):
        result = await self.corkus.player.search("MrBartusekXD")
        self.assertTrue(any(p.username == "MrBartusekXD" for p in result))

    @vcr.use_cassette
    async def test_guild(self):
        result = await self.corkus.guild.search("farplane")
        self.assertTrue(any(g.name == "The Farplane" for g in result))

    async def asyncTearDown(self):
        await self.corkus.close()
