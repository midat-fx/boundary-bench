import unittest

from intervals.merge import merge_ranges


class MergeTest(unittest.TestCase):
    def test_overlap(self):
        self.assertEqual(merge_ranges([(1, 4), (2, 6)]), [(1, 6)])

    def test_disjoint(self):
        self.assertEqual(merge_ranges([(5, 6), (1, 2)]), [(1, 2), (5, 6)])
