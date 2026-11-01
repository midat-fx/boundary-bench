import unittest

from app.release import bump


class Hidden(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(bump("1.4.7", "minor"), "1.5.0")
        self.assertEqual(bump("1.4.7", "major"), "2.0.0")
        self.assertEqual(bump("0.9.9", "patch"), "0.9.10")
        with self.assertRaises(ValueError):
            bump("1.0.0", "build")
