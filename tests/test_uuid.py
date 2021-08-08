# pylint: disable=attribute-defined-outside-init

import unittest
from corkus.objects import CorkusUUID

class TestPlaytime(unittest.TestCase):
    def setUp(self):
        self.uuid = CorkusUUID("0edc3eb6-74d8-49b6-8b2a-3c0782183e3a")

    def test_dashed(self):
        self.assertEqual(self.uuid.string(True), "0edc3eb6-74d8-49b6-8b2a-3c0782183e3a")

    def test_undashed(self):
        self.assertEqual(self.uuid.string(False), "0edc3eb674d849b68b2a3c0782183e3a")
