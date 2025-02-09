import os
import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill

def create_spreadsheet(file_path):
    """
    Create a new spreadsheet with headers for transactions if it does not already exist.

    Args:
        file_path (str): Path to the file to create.
    """
    if not os.path.exists(file_path):
        # Define the headers for the spreadsheet
        headers = ['Date', 'Description', 'Transaction', 'Debit', 'Credit', 'Balance']

        # Create an empty DataFrame with the headers
        df = pd.DataFrame(columns=headers)

        # Save the DataFrame to an Excel file
        df.to_excel(file_path, index=False)
def add_transaction(file_path, date, description, transaction, debit, credit, reconciled=False):
    """
    Add a transaction to the spreadsheet.

    Args:
        file_path (str): Path to the spreadsheet file.
        date (str): Date of the transaction.
        description (str): Description of the transaction.
        transaction (str): Transaction identifier.
        debit (float): Debit amount of the transaction.
        credit (float): Credit amount of the transaction.
        reconciled (bool): Flag to indicate if the transaction has been reconciled.
    """
    # Load the existing spreadsheet into a DataFrame
    try:
        df = pd.read_excel(file_path)
    except FileNotFoundError:
        # If the file does not exist, create a new DataFrame with headers
        df = pd.DataFrame(columns=['Date', 'Description', 'Transaction', 'Debit', 'Credit', 'Balance', 'Reconciled'])

    # Calculate the new balance
    if len(df) == 0:
        balance = credit - debit
    else:
        balance = df['Balance'].iloc[-1] + credit - debit

    # Create a new transaction as a DataFrame
    new_txn = pd.DataFrame([{
        'Date': date,
        'Description': description,
        'Transaction': transaction,
        'Debit': debit,
        'Credit': credit,
        'Balance': balance,
        'Reconciled': reconciled

    }])

    # Append the new transaction to the DataFrame
    df = pd.concat([df, new_txn], ignore_index=True)

    # Save the updated DataFrame back to the Excel file
    df.to_excel(file_path, index=False)

    # Apply formatting to the Excel file
    apply_formatting(file_path)

def apply_formatting(file_path):
    """
    Apply formatting to the Excel file.

    Args:
        file_path (str): Path to the Excel file.
    """
    wb = load_workbook(file_path)
    ws = wb.active

    # Apply red font to debit values
    red_font = Font(color="FF0000")
    for row in ws.iter_rows(min_row=2, min_col=4, max_col=4):
        for cell in row:
            if cell.value < 0:
                cell.font = red_font

    wb.save(file_path)