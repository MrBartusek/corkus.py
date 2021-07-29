# pylint: disable=attribute-defined-outside-init

import unittest
from corkus import Corkus
from corkus.objects import CorkusUUID, PlayerRank, PartialPlayer

class TestPlayer(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.corkus = Corkus()

    async def test_player_get_uuid(self):
        uuid = await self.corkus.player.get_uuid('Salted')
        self.assertEqual(uuid, CorkusUUID('1ed075fc-5aa9-42e0-a29f-640326c1d80c'))

    async def test_player_get_stats_uuid(self):
        user = await self.corkus.player.get(CorkusUUID('1ed075fc-5aa9-42e0-a29f-640326c1d80c'))
        self.assertEqual(user.rank, PlayerRank.ADMINISTRATOR)

    async def test_player_get_stats_username(self):
        user = await self.corkus.player.get('Salted')
        self.assertEqual(user.rank, PlayerRank.ADMINISTRATOR)

    async def test_fetch_partial(self):
        partial = PartialPlayer(self.corkus, username = "Salted")
        user = await partial.fetch()
        self.assertEqual(user.rank, PlayerRank.ADMINISTRATOR)

    async def asyncTearDown(self):
        await self.corkus.close()
