# pylint: disable=attribute-defined-outside-init

import unittest
from tests import vcr
from corkus import Corkus

class TestRatelimit(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.corkus = Corkus()

    @vcr.use_cassette
    async def test_ratelimit(self):
        await self.corkus.ingredient.get("Glow Bulb Seeds")
        self.assertLess(self.corkus.request.ratelimit.remaining, self.corkus.request.ratelimit.total)

    async def asyncTearDown(self):
        await self.corkus.close()
