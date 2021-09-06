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
    async def test_network_player_sum(self):
        response = await self.corkus.network.players_sum()
        self.assertGreaterEqual(response, 1)

    @vcr.use_cassette
    async def test_network_servers_list(self):
        response = await self.corkus.network.online_players()
        self.assertGreater(sum([s.total_players for s in response.servers]), 0)
        self.assertTrue(any(s.name.startswith("WC") for s in response.servers))
        self.assertTrue(any(s.type == ServerType.STANDARD for s in response.servers))
        self.assertGreater(len(response.players), 0)

    @vcr.use_cassette
    async def test_network_online_status(self):
        response = await self.corkus.network.online_players()
        player = await response.players[0].fetch()
        self.assertTrue(player.status.online)
        self.assertTrue(player.online)
        self.assertEqual(player.status.server.name, response.servers[0].name)
        diff = abs(int(player.last_online.timestamp()) - int(time.time()))
        self.assertTrue(10 >= diff >= 0)

    @vcr.use_cassette
    async def test_network_helpers(self):
        response = await self.corkus.network.online_players()
        player = response.players[0]
        self.assertTrue(response.is_player_online(player))
        self.assertEqual(response.get_player_server(player).name, response.servers[0].name)

    async def asyncTearDown(self):
        await self.corkus.close()
