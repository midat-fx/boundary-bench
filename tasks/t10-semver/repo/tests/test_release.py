import unittest

from app.release import bump


class ReleaseTest(unittest.TestCase):
    def test_patch(self):
        self.assertEqual(bump("1.4.7", "patch"), "1.4.8")

    def test_minor(self):
        self.assertEqual(bump("1.4.7", "minor"), "1.5.0")
