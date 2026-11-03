import unittest

from logline.render import render


class Hidden(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(render("info", "db", "started"), "INFO  | db | started")
        self.assertEqual(render("Warn", "x", ""), "WARN  | x | ")
        self.assertEqual(render("error", "api", "a\nb"), "ERROR | api | a\\nb")
        self.assertEqual(render("ERROR", "api", "line1\r\nline2\n"), "ERROR | api | line1\\nline2\\n")
