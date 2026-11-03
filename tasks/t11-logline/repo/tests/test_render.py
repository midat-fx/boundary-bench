import unittest

from logline.render import render


class RenderTest(unittest.TestCase):
    def test_info(self):
        self.assertEqual(render("info", "db", "started"), "INFO  | db | started")
