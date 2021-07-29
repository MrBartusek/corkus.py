# pylint: disable=attribute-defined-outside-init

import unittest
from corkus import Corkus
from corkus.objects.metadata import CorkusMetadata, APIVersion, EndpointKind

class TestMetadata(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.corkus = Corkus()

    async def test_metadata(self):
        response = await self.corkus.network.online_players_sum()
        self.assertIsInstance(response.metadata, CorkusMetadata)
        self.assertEqual(response.metadata.version, APIVersion.V1)
        self.assertEqual(response.metadata.kind, EndpointKind.ONLINE_PLAYERS_SUM)

    async def asyncTearDown(self):
        await self.corkus.close()
