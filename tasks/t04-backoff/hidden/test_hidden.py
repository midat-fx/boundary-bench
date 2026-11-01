import unittest

from retry.backoff import backoff_delays


class Hidden(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(backoff_delays(6, 1, 10), [1, 2, 4, 8, 10, 10])
        self.assertEqual(backoff_delays(4, 3, 5), [3, 5, 5, 5])
        self.assertEqual(backoff_delays(0, 1, 1), [])
        self.assertEqual(backoff_delays(3, 0.5, 100), [0.5, 1, 2])
