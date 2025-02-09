import os
import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

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

def carry_balance_to_next_month(file_path):
    """
    Carry the balance at the end of the month to the next month as the starting balance.

    Args:
        file_path (str): Path to the spreadsheet file.
    """
    # Load the existing spreadsheet into a DataFrame
    df = pd.read_excel(file_path)

    # Get the last balance
    last_balance = df['Balance'].iloc[-1]

    # Get the last date
    last_date = pd.to_datetime(df['Date'].iloc[-1])

    # Calculate the first date of the next month
    next_month_date = (last_date + pd.offsets.MonthBegin(1)).strftime('%Y-%m-%d')

    # Create a new transaction for the starting balance of the next month
    new_txn = pd.DataFrame([{
        'Date': next_month_date,
        'Description': 'Starting Balance',
        'Transaction': '',
        'Debit': 0.0,
        'Credit': 0.0,
        'Balance': last_balance,
        'Reconciled': False
    }])

    # Append the new transaction to the DataFrame
    df = pd.concat([df, new_txn], ignore_index=True)

    # Save the updated DataFrame back to the Excel file
    df.to_excel(file_path, index=False)

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

def generate_monthly_report(file_path, month, year):
    """
    Generate a monthly report summarizing transactions for a given month.

    Args:
        file_path (str): Path to the spreadsheet file.
        month (int): Month for which to generate the report.
        year (int): Year for which to generate the report.
    """
    # Load the existing spreadsheet into a DataFrame
    df = pd.read_excel(file_path)

    # Specify the date format explicitly
    df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d', errors='coerce')

    # Filter transactions for the given month and year
    monthly_df = df[(df['Date'].dt.month == month) & (df['Date'].dt.year == year)]

    # Summarize transactions
    total_debit = monthly_df['Debit'].sum()
    total_credit = monthly_df['Credit'].sum()
    ending_balance = monthly_df['Balance'].iloc[-1] if not monthly_df.empty else 0.0

    # Create a summary DataFrame
    summary_df = pd.DataFrame([{
        'Month': month,
        'Year': year,
        'Total Debit': total_debit,
        'Total Credit': total_credit,
        'Ending Balance': ending_balance
    }])

    # Save the summary DataFrame to an Excel file
    report_file_path = f"data/monthly_report_{year}_{month}.pdf"
    c = canvas.Canvas(report_file_path, pagesize=letter)
    c.drawString(100, 750, f"Monthly Report for {month}/{year}")
    c.drawString(100, 730, f"Total Debit: {total_debit}")
    c.drawString(100, 710, f"Total Credit: {total_credit}")
    c.drawString(100, 690, f"Ending Balance: {ending_balance}")
    c.save()