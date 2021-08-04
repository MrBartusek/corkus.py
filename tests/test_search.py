# pylint: disable=attribute-defined-outside-init

from datetime import datetime
import unittest
from corkus import Corkus

class TestSearch(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.corkus = Corkus()

    async def test_guilds_and_players(self):
        result = await self.corkus.search.guilds_and_players("MrBartusekXD")
        self.assertTrue(any(p.username == "MrBartusekXD" for p in result.players))

        result = await self.corkus.search.guilds_and_players("farplane")
        self.assertTrue(any(g.name == "The Farplane" for g in result.guilds))

    async def test_players(self):
        result = await self.corkus.player.search("MrBartusekXD")
        self.assertTrue(any(p.username == "MrBartusekXD" for p in result))

    async def test_guild(self):
        result = await self.corkus.guild.search("farplane")
        self.assertTrue(any(g.name == "The Farplane" for g in result))

    async def asyncTearDown(self):
        await self.corkus.close()
