# filepath: bank-reconciliation-app/src/utils/helpers.py

import pandas as pd

def create_spreadsheet(file_path):
    """
    Create a new spreadsheet with headers for transactions.

    Args:
        file_path (str): Path to the file to create.
    """
    # Define the headers for the spreadsheet
    headers = ['Date', 'Description', 'Transaction', 'Type', 'Amount', 'Balance']

    # Create an empty DataFrame with the headers
    df = pd.DataFrame(columns=headers)

    # Save the DataFrame to an Excel file
    df.to_excel(file_path, index=False)

def add_transaction(file_path, date, description, transaction, txn_type, amount):
    """
    Add a transaction to the spreadsheet.

    Args:
        file_path (str): Path to the spreadsheet file.
        date (str): Date of the transaction.
        description (str): Description of the transaction.
        transaction (str): Transaction identifier.
        txn_type (str): Type of the transaction ('Withdrawal' or 'Deposit').
        amount (float): Amount of the transaction.
    """
    # Load the existing spreadsheet into a DataFrame
    df = pd.read_excel(file_path)

    # Calculate the new balance
    if len(df) == 0:
        balance = amount
    else:
        balance = df.iloc[-1]['Balance'] + amount if txn_type == 'Deposit' else df.iloc[-1]['Balance'] - amount

    # Create a new transaction as a DataFrame
    new_txn = pd.DataFrame([{
        'Date': date,
        'Description': description,
        'Transaction': transaction,
        'Type': txn_type,
        'Amount': amount,
        'Balance': balance
    }])

      # Append the new transaction to the DataFrame
    if df.empty:
        df = new_txn
    else:
        df = pd.concat([df, new_txn], ignore_index=True)

    # Save the updated DataFrame back to the Excel file
    df.to_excel(file_path, index=False)