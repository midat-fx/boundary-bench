import unittest

from parse.fields import split_fields


class FieldsTest(unittest.TestCase):
    def test_plain(self):
        self.assertEqual(split_fields("a,b,c"), ["a", "b", "c"])

    def test_quoted_comma(self):
        self.assertEqual(split_fields('a,"b,c",d'), ["a", "b,c", "d"])
