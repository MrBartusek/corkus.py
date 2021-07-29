# pylint: disable=attribute-defined-outside-init

import unittest
from corkus import Corkus

class TestNetwork(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.corkus = Corkus()

    async def test_player_sum(self):
        response = await self.corkus.network.online_players_sum()
        self.assertGreaterEqual(response.players_sum, 1)
        self.assertEqual(int(response), response.players_sum)

    async def asyncTearDown(self):
        await self.corkus.close()
