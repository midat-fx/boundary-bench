import unittest

from billing.total import invoice_total


class TotalTest(unittest.TestCase):
    def test_no_discount(self):
        self.assertEqual(invoice_total([(1000, 2)], 0, 10), 2200)

    def test_discount_then_tax(self):
        self.assertEqual(invoice_total([(1000, 1)], 50, 10), 550)
