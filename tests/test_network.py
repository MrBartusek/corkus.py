# pylint: disable=attribute-defined-outside-init

import unittest
import time
from tests import vcr
from corkus import Corkus
from corkus.objects import ServerType

class TestNetwork(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.corkus = Corkus()

    @vcr.use_cassette
    async def test_player_sum(self):
        response = await self.corkus.network.players_sum()
        self.assertGreaterEqual(response, 1)

    @vcr.use_cassette
    async def test_servers_list(self):
        response = await self.corkus.network.servers_list()
        self.assertGreaterEqual(sum([s.total_players for s in response]), 1)
        self.assertTrue(any(s.name.startswith("WC") for s in response))
        self.assertTrue(any(s.type == ServerType.STANDARD for s in response))

    @vcr.use_cassette
    async def test_online_status(self):
        response = await self.corkus.network.servers_list()
        player = await response[0].players[0].fetch()
        self.assertTrue(player.status.online)
        self.assertTrue(player.online)
        self.assertEqual(player.status.server.name, response[0].name)
        diff = abs(int(player.last_online.timestamp()) - int(time.time()))
        self.assertTrue(10 >= diff >= 0)

    async def asyncTearDown(self):
        await self.corkus.close()
