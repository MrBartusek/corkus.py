# pylint: disable=attribute-defined-outside-init

from datetime import datetime
import unittest
from tests import vcr
from corkus import Corkus

class TestTerritory(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.corkus = Corkus()

    @vcr.use_cassette
    async def test_all_territories(self):
        all_territories = await self.corkus.territory.list_all()
        Territory = all_territories[0]
        self.assertTrue(any(g.name == "Detlas" for g in all_territories))
        self.assertTrue(Territory.acquired > datetime(2013, 4, 29, 0, 0, 0))
        self.assertNotEqual(Territory.location.start_x, 0)
        self.assertNotEqual(Territory.location.start_y, 0)
        self.assertNotEqual(Territory.location.end_x, 0)
        self.assertNotEqual(Territory.location.end_y, 0)
        self.assertGreater(len(Territory.guild.name), 0)

    @vcr.use_cassette
    async def test_partial_Territory(self):
        all_territories = await self.corkus.territory.list_all()
        Territory = all_territories[0]
        guild = await Territory.guild.fetch()
        self.assertGreater(len(guild.territories), 0)
        self.assertGreater(guild.territories.count, 0)
        guild_teritories = await guild.territories.fetch()
        self.assertTrue(any(g.name == Territory.name for g in guild_teritories))

    async def asyncTearDown(self):
        await self.corkus.close()
