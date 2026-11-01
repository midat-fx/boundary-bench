import unittest

from billing.total import invoice_total


class Hidden(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(invoice_total([(1000, 1)], 50, 10), 550)
        self.assertEqual(invoice_total([(250, 4), (500, 2)], 20, 25), 2000)
        self.assertEqual(invoice_total([(999, 3)], 0, 0), 2997)
        self.assertEqual(invoice_total([], 10, 10), 0)
