# pylint: disable=attribute-defined-outside-init, protected-access

import unittest
from tests import vcr
import time
from corkus import Corkus

class TestCache(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.corkus = Corkus()

    @vcr.use_cassette
    async def test_cache(self):
        self.assertEqual(len(self.corkus._request.cache.content), 0)
        await self.corkus.ingredient.get("Glow Bulb Seeds")
        self.assertEqual(len(self.corkus._request.cache.content), 1)
        element = self.corkus._request.cache.get("https://api.wynncraft.com/v2/ingredient/get/Glow_Bulb_Seeds")
        self.assertGreater(element.valid_timestamp, time.time() + 30)

    async def asyncTearDown(self):
        await self.corkus.close()
