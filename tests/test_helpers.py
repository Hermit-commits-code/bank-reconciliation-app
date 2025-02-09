# Content for /bank-reconciliation-app/bank-reconciliation-app/tests/test_helpers.py

import unittest
from src.utils.helpers import format_transaction, calculate_difference

class TestHelpers(unittest.TestCase):

    def test_format_transaction(self):
        # Test case for formatting a transaction
        transaction = {'date': '2023-01-01', 'amount': 100.0, 'description': 'Deposit'}
        formatted = format_transaction(transaction)
        expected = '2023-01-01: Deposit - $100.00'
        self.assertEqual(formatted, expected)

    def test_calculate_difference(self):
        # Test case for calculating the difference between two amounts
        amount1 = 150.0
        amount2 = 100.0
        difference = calculate_difference(amount1, amount2)
        expected_difference = 50.0
        self.assertEqual(difference, expected_difference)

if __name__ == '__main__':
    unittest.main()