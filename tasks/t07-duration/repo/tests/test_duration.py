import unittest

from timeparse.duration import parse_duration


class DurationTest(unittest.TestCase):
    def test_single_unit(self):
        self.assertEqual(parse_duration("2h"), 7200)
        self.assertEqual(parse_duration("45m"), 2700)
