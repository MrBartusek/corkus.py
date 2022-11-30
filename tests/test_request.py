# pylint: disable=attribute-defined-outside-init

import unittest
from tests import vcr
from corkus import Corkus
from corkus.errors import CorkusTimeoutError

class TestRequest(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.corkus = Corkus()

    @vcr.use_cassette
    async def test_timeout(self):
        with self.assertRaises(CorkusTimeoutError) as context:
            # pylint: disable=protected-access
            request = self.corkus._request
            await request.get(None, "https://httpstat.us/200?sleep=5000", 1)
        exception = context.exception
        self.assertEqual(exception.timeout, 1)
        self.assertEqual(exception.url, "https://httpstat.us/200?sleep=5000")

    async def asyncTearDown(self):
        await self.corkus.close()
