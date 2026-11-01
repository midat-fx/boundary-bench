import unittest

from intervals.merge import merge_ranges


class Hidden(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(merge_ranges([(1, 3), (3, 5)]), [(1, 5)])
        self.assertEqual(merge_ranges([(3, 5), (1, 3), (8, 9)]), [(1, 5), (8, 9)])
        self.assertEqual(merge_ranges([(1, 2), (4, 5)]), [(1, 2), (4, 5)])
        self.assertEqual(merge_ranges([]), [])
