import unittest

from app.stats import average_kelvin, percent


class StatsTest(unittest.TestCase):
    def test_percent(self):
        self.assertEqual(percent(1, 4), 25.0)

    def test_average_kelvin(self):
        self.assertEqual(average_kelvin([(0, "C"), (273.15, "K")]), 273.15)
