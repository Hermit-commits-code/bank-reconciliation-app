# Contents of /bank-reconciliation-app/bank-reconciliation-app/src/reconciliation/reconcile.py

"""
This module contains the core functionality for reconciling bank statements.
It includes classes and functions that handle the logic for comparing transactions
and identifying discrepancies.
"""

class Transaction:
    def __init__(self, date, description, amount):
        self.date = date
        self.description = description
        self.amount = amount

    def __repr__(self):
        return f"Transaction(date={self.date}, description='{self.description}', amount={self.amount})"


class Reconciliation:
    def __init__(self, bank_transactions, book_transactions):
        self.bank_transactions = bank_transactions
        self.book_transactions = book_transactions
        self.discrepancies = []

    def reconcile(self):
        bank_set = set((t.date, t.description, t.amount) for t in self.bank_transactions)
        book_set = set((t.date, t.description, t.amount) for t in self.book_transactions)

        # Find discrepancies
        self.discrepancies = list(bank_set.symmetric_difference(book_set))

    def get_discrepancies(self):
        return self.discrepancies


def load_transactions_from_file(file_path):
    transactions = []
    with open(file_path, 'r') as file:
        for line in file:
            date, description, amount = line.strip().split(',')
            transactions.append(Transaction(date, description, float(amount)))
    return transactions


def main(bank_file, book_file):
    bank_transactions = load_transactions_from_file(bank_file)
    book_transactions = load_transactions_from_file(book_file)

    reconciliation = Reconciliation(bank_transactions, book_transactions)
    reconciliation.reconcile()

    discrepancies = reconciliation.get_discrepancies()
    if discrepancies:
        print("Discrepancies found:")
        for discrepancy in discrepancies:
            print(discrepancy)
    else:
        print("No discrepancies found.")


if __name__ == "__main__":
    # Example usage:
    # main('bank_transactions.csv', 'book_transactions.csv')
    pass  # This line is a placeholder for future implementation.