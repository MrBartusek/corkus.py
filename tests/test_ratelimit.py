# pylint: disable=attribute-defined-outside-init

import unittest
from tests import vcr
from corkus import Corkus

class TestRatelimit(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.corkus = Corkus()
        await self.corkus.start()

    @vcr.use_cassette
    async def test_ratelimit(self):
        await self.corkus.ingredient.get("Glow Bulb Seeds")
        self.assertLess(self.corkus.rate_limit.remaining, self.corkus.rate_limit.total)
        self.assertLessEqual(self.corkus.rate_limit.reset, 60)

    async def asyncTearDown(self):
        await self.corkus.close()
