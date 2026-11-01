import unittest

from textkit.slug import slugify


class Hidden(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(slugify("Hello,  World!"), "hello-world")
        self.assertEqual(slugify("  --Already-Slugged--  "), "already-slugged")
        self.assertEqual(slugify("a__b..c"), "a-b-c")
        self.assertEqual(slugify("Python 3.12"), "python-3-12")
