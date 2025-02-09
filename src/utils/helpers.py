def format_currency(amount):
    """Formats a numeric amount as currency."""
    return "${:,.2f}".format(amount)

def calculate_difference(statement_total, transaction_total):
    """Calculates the difference between the statement total and the transaction total."""
    return statement_total - transaction_total

def parse_transaction_line(line):
    """Parses a line from a transaction file and returns a dictionary with relevant details."""
    parts = line.strip().split(',')
    return {
        'date': parts[0],
        'description': parts[1],
        'amount': float(parts[2]),
    }

def validate_transaction(transaction):
    """Validates a transaction to ensure it has the required fields."""
    required_fields = ['date', 'description', 'amount']
    for field in required_fields:
        if field not in transaction:
            raise ValueError(f"Missing required field: {field}")
    return True

def summarize_transactions(transactions):
    """Summarizes a list of transactions, returning the total amount."""
    return sum(transaction['amount'] for transaction in transactions)