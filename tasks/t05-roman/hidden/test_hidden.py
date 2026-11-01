import unittest

from roman.convert import to_roman


class Hidden(unittest.TestCase):
    def test_cases(self):
        for n, want in [(3, "III"), (4, "IV"), (49, "XLIX"), (444, "CDXLIV"), (3999, "MMMCMXCIX"), (2024, "MMXXIV")]:
            self.assertEqual(to_roman(n), want)
        with self.assertRaises(ValueError):
            to_roman(0)
