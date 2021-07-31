# pylint: disable=attribute-defined-outside-init

from datetime import datetime
import unittest
from corkus import Corkus

class TestGuild(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.corkus = Corkus()

    async def test_all_territories(self):
        all_territories = await self.corkus.territory.list_all()
        teritory = all_territories[0]
        self.assertTrue(any([g.name == "Detlas" for g in all_territories]))
        self.assertTrue(teritory.acquired > datetime(2013, 4, 29, 0, 0, 0))
        self.assertNotEqual(teritory.location.start_x, 0)
        self.assertNotEqual(teritory.location.start_y, 0)
        self.assertNotEqual(teritory.location.end_x, 0)
        self.assertNotEqual(teritory.location.end_y, 0)
        self.assertGreater(len(teritory.guild.name), 0)

    async def asyncTearDown(self):
        await self.corkus.close()
