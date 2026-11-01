import unittest

from stats.words import top_words


class Hidden(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(list(top_words("b a c b a", 2)), [("a", 2), ("b", 2)])
        self.assertEqual(list(top_words("Z z y X x x", 3)), [("x", 3), ("z", 2), ("y", 1)])
        self.assertEqual(list(top_words("", 3)), [])
