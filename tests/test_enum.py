# pylint: disable=attribute-defined-outside-init

import unittest
from corkus.objects import PlayerTag

class TestEnum(unittest.TestCase):
    def test_enum_int(self):
        self.assertEqual(int(PlayerTag.VIP), 1)

    def test_enum_eq(self):
        self.assertEqual(PlayerTag.VIP, PlayerTag.VIP)
        self.assertNotEqual(PlayerTag.VIP, 1)

    def test_enum_compare(self):
        self.assertGreater(PlayerTag.CHAMPION, PlayerTag.HERO)
        self.assertLess(PlayerTag.VIP, PlayerTag.HERO)
