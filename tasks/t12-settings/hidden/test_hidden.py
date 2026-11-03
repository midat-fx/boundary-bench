import os
import tempfile
import unittest

from uploader.settings import DEFAULTS, load_settings


class Hidden(unittest.TestCase):
    def test_repo_file(self):
        s = load_settings()
        self.assertEqual(s, {"retries": 5, "timeout_s": 2.5})
        self.assertIs(type(s["retries"]), int)
        self.assertIs(type(s["timeout_s"]), float)

    def test_partial_and_missing_file(self):
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, "s.ini")
            with open(path, "w") as f:
                f.write("[upload]\nretries = 7\n")
            self.assertEqual(load_settings(path), {"retries": 7, "timeout_s": 10.0})
            self.assertEqual(load_settings(os.path.join(d, "none.ini")), DEFAULTS)
