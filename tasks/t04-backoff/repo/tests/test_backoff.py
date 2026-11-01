import unittest

from retry.backoff import backoff_delays


class BackoffTest(unittest.TestCase):
    def test_growth(self):
        self.assertEqual(backoff_delays(3, 1, 100), [1, 2, 4])

    def test_cap(self):
        self.assertEqual(backoff_delays(6, 1, 10), [1, 2, 4, 8, 10, 10])
