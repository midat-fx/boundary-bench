import unittest

from uploader.settings import load_settings


class SettingsTest(unittest.TestCase):
    def test_retries_is_a_number(self):
        self.assertEqual(load_settings()["retries"] + 1, 6)
