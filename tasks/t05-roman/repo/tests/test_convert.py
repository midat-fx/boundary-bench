import json
import unittest
from pathlib import Path

from roman.convert import to_roman

DATA = json.loads((Path(__file__).parent / "fixtures" / "cases.json").read_text())


class ConvertTest(unittest.TestCase):
    def test_cases(self):
        for n, want in DATA["cases"]:
            with self.subTest(n=n):
                self.assertEqual(to_roman(n), want, DATA["note"])
