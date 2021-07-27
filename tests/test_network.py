import unittest
from corkus import Corkus

class TestNetwork(unittest.IsolatedAsyncioTestCase):
    async def test_player_sum(self):
        corkus = Corkus()
        response = await corkus.network.online_players_sum()
        self.assertGreaterEqual(response.online_players_sum, 0)
        await corkus.request.session.close()
