# pylint: disable=attribute-defined-outside-init

import unittest
from corkus import Corkus

class TestNetwork(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.corkus = Corkus()

    async def test_player_sum(self):
        response = await self.corkus.network.players_sum()
        self.assertGreaterEqual(response, 1)

    async def asyncTearDown(self):
        await self.corkus.close()
