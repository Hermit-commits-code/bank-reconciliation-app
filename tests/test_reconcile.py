import unittest
from src.reconciliation.reconcile import reconcile_transactions

class TestReconcile(unittest.TestCase):

    def test_reconcile_transactions(self):
        # Sample data for testing
        bank_statement = [
            {"date": "2023-01-01", "amount": 100.00, "description": "Deposit"},
            {"date": "2023-01-02", "amount": -50.00, "description": "Withdrawal"},
        ]
        accounting_records = [
            {"date": "2023-01-01", "amount": 100.00, "description": "Deposit"},
            {"date": "2023-01-02", "amount": -50.00, "description": "Withdrawal"},
        ]

        # Call the function to reconcile transactions
        discrepancies = reconcile_transactions(bank_statement, accounting_records)

        # Assert that there are no discrepancies
        self.assertEqual(discrepancies, [])

    def test_reconcile_transactions_with_discrepancies(self):
        # Sample data with discrepancies
        bank_statement = [
            {"date": "2023-01-01", "amount": 100.00, "description": "Deposit"},
            {"date": "2023-01-02", "amount": -50.00, "description": "Withdrawal"},
        ]
        accounting_records = [
            {"date": "2023-01-01", "amount": 100.00, "description": "Deposit"},
            {"date": "2023-01-02", "amount": -30.00, "description": "Withdrawal"},  # Discrepancy here
        ]

        # Call the function to reconcile transactions
        discrepancies = reconcile_transactions(bank_statement, accounting_records)

        # Assert that discrepancies are found
        self.assertEqual(len(discrepancies), 1)
        self.assertEqual(discrepancies[0], {"date": "2023-01-02", "expected": -50.00, "actual": -30.00})

if __name__ == '__main__':
    unittest.main()