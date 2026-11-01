import json
import unittest
from pathlib import Path

from stats.words import top_words

CASE = json.loads((Path(__file__).parent / "fixtures" / "expected.json").read_text())


class WordsTest(unittest.TestCase):
    def test_ties_alphabetical(self):
        got = [list(p) for p in top_words(CASE["text"], CASE["n"])]
        self.assertEqual(got, CASE["expected"], CASE["comment"])
