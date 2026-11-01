import unittest

from parse.fields import split_fields


class Hidden(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(split_fields('a,"b,c",d'), ["a", "b,c", "d"])
        self.assertEqual(split_fields('"x,y,z"'), ["x,y,z"])
        self.assertEqual(split_fields("a,,b"), ["a", "", "b"])
        self.assertEqual(split_fields('1,"2,3",4,"5"'), ["1", "2,3", "4", "5"])
