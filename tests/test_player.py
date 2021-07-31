# pylint: disable=attribute-defined-outside-init

import unittest
from corkus import Corkus
from corkus.objects import CorkusUUID, PartialPlayer

class TestPlayer(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.corkus = Corkus()

    async def test_player_get_uuid(self):
        uuid = await self.corkus.player.get_uuid('MrBartusekXD')
        self.assertEqual(uuid, CorkusUUID('0edc3eb6-74d8-49b6-8b2a-3c0782183e3a'))

    async def test_player_get_stats_uuid(self):
        player = await self.corkus.player.get(CorkusUUID('0edc3eb6-74d8-49b6-8b2a-3c0782183e3a'))
        self.assertEqual(player.username, "MrBartusekXD")

    async def test_fetch_partial(self):
        partial = PartialPlayer(self.corkus, username = "MrBartusekXD")
        player = await partial.fetch()
        self.assertEqual(player.uuid, CorkusUUID('0edc3eb6-74d8-49b6-8b2a-3c0782183e3a'))

    async def test_player_get_stats_username(self):
        player = await self.corkus.player.get('MrBartusekXD')
        self.assertEqual(player.uuid, CorkusUUID('0edc3eb6-74d8-49b6-8b2a-3c0782183e3a'))
        self.assertEqual(player.member.username, "MrBartusekXD")
        self.assertEqual(player.guild.name, "The Farplane")

    async def asyncTearDown(self):
        await self.corkus.close()