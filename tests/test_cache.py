# pylint: disable=attribute-defined-outside-init

import unittest
from tests import vcr
import time
from corkus import Corkus
from corkus.utils.constants import URL_V2

class TestCache(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.corkus = Corkus()

    @vcr.use_cassette
    async def test_cache(self):
        self.assertEqual(len(self.corkus.request.cache.content), 0)
        await self.corkus.ingredient.get("Glow Bulb Seeds")
        self.assertEqual(len(self.corkus.request.cache.content), 1)
        element = self.corkus.request.cache.get(URL_V2 + "ingredient/get/Glow_Bulb_Seeds")
        self.assertGreater(element.valid_timestamp, time.time() + 30)

    async def asyncTearDown(self):
        await self.corkus.close()
