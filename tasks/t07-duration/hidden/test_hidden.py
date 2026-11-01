import unittest

from timeparse.duration import parse_duration


class Hidden(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(parse_duration("1h30m"), 5400)
        self.assertEqual(parse_duration("1h2m3s"), 3723)
        self.assertEqual(parse_duration("45m"), 2700)
        self.assertEqual(parse_duration("10s"), 10)
