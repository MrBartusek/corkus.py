# pylint: disable=attribute-defined-outside-init

import unittest
from corkus import Corkus
from corkus.objects import ServerType

class TestNetwork(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.corkus = Corkus()

    async def test_player_sum(self):
        response = await self.corkus.network.players_sum()
        self.assertGreaterEqual(response, 1)

    async def test_servers_list(self):
        response = await self.corkus.network.servers_list()
        self.assertGreaterEqual(sum([s.total_players for s in response]), 1)
        self.assertTrue(any([s.name.startswith("WC") for s in response]))
        self.assertTrue(any([s.type == ServerType.STANDARD for s in response]))

    async def asyncTearDown(self):
        await self.corkus.close()
