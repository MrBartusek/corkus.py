# pylint: disable=attribute-defined-outside-init

import unittest
from tests import vcr
from corkus import Corkus
from corkus.errors import CorkusException

class TestCorkus(unittest.IsolatedAsyncioTestCase):
    @vcr.use_cassette
    async def test_context_manager(self):
        async with Corkus() as corkus:
            player = await corkus.player.get('MrBartusekXD')
            self.assertEqual(player.username, 'MrBartusekXD')

    async def test_initialize(self):
        corkus = Corkus()
        with self.assertRaises(CorkusException):
            await corkus.player.get('MrBartusekXD')
