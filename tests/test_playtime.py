# pylint: disable=attribute-defined-outside-init

import unittest
from corkus.objects.playtime import PlayerPlaytime, PlaytimeConvertRatio

class TestPlaytime(unittest.TestCase):
    def setUp(self):
        self.playtime = PlayerPlaytime(1000)

    def test_playtime_raw(self):
        self.assertEqual(self.playtime.raw, 1000)

    def test_playtime_preset(self):
        self.assertEqual(self.playtime.minutes(PlaytimeConvertRatio.WYNNDATA), 1000 * 5)

    def test_playtime_value(self):
        self.assertEqual(self.playtime.minutes(1.0), 1000)

    def test_playtime_hours(self):
        self.assertEqual(self.playtime.hours(PlaytimeConvertRatio.RAW), 1000 / 60)
