import unittest

from app.stats import average_kelvin


class Hidden(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(average_kelvin([(0, "C"), (273.15, "K")]), 273.15)
        self.assertEqual(average_kelvin([(32, "F"), (100, "C")]), 323.15)
        self.assertEqual(average_kelvin([(212, "F")]), 373.15)
        self.assertIsNone(average_kelvin([]))
        with self.assertRaises(ValueError):
            average_kelvin([(1, "X")])
