# filepath: bank-reconciliation-app/src/main.py
import os
import tkinter as tk
from tkinter import messagebox
from utils.helpers import create_spreadsheet, add_transaction,carry_balance_to_next_month, generate_monthly_report, export_transactions_to_csv


def add_transaction_ui():
    """
    Function to add a transaction through the UI.
    """
    date = date_entry.get()
    description = description_entry.get()
    transaction = transaction_entry.get()
    debit = float(debit_entry.get()) if debit_entry.get() else 0.0
    credit = float(credit_entry.get()) if credit_entry.get() else 0.0
    reconciled = reconciled_var.get()

    add_transaction(spreadsheet_path, date, description, transaction, debit, credit, reconciled)
    messagebox.showinfo("Success", "Transaction added successfully!")

def carry_balance_ui():
    """
    Function to carry the balance to the next month through the UI.
    """
    carry_balance_to_next_month(spreadsheet_path)
    messagebox.showinfo("Success", "Balance carried to the next month successfully!")

def generate_report_ui():
    """
    Function to generate a monthly report through the UI.
    """
    month = int(month_entry.get())
    year = int(year_entry.get())
    generate_monthly_report(spreadsheet_path, month, year)
    messagebox.showinfo("Success", f"Monthly report for {month}/{year} generated successfully!")

def export_transactions_ui():
    """
    Function to export all transactions to a CSV file through the UI.
    """
    export_transactions_to_csv(spreadsheet_path)
    messagebox.showinfo("Success", "Transactions exported to CSV successfully!")

def main():
    """
    Main function to run the bank reconciliation application.
    """
    global spreadsheet_path
    spreadsheet_path = 'data/transactions.xlsx'

    # Ensure the data directory exists
    os.makedirs(os.path.dirname(spreadsheet_path), exist_ok=True)

    # Create a new spreadsheet with headers
    create_spreadsheet(spreadsheet_path)

    # Initialize the main window
    root = tk.Tk()
    root.title("Bank Reconciliation Application")

    # Create UI elements for transaction entry
    tk.Label(root, text="Date").grid(row=0, column=0)
    global date_entry
    date_entry = tk.Entry(root)
    date_entry.grid(row=0, column=1)

    tk.Label(root, text="Description").grid(row=1, column=0)
    global description_entry
    description_entry = tk.Entry(root)
    description_entry.grid(row=1, column=1)

    tk.Label(root, text="Payee").grid(row=2, column=0)
    global transaction_entry
    transaction_entry = tk.Entry(root)
    transaction_entry.grid(row=2, column=1)

    tk.Label(root, text="Debit").grid(row=3, column=0)
    global debit_entry
    debit_entry = tk.Entry(root)
    debit_entry.grid(row=3, column=1)

    tk.Label(root, text="Credit").grid(row=4, column=0)
    global credit_entry
    credit_entry = tk.Entry(root)
    credit_entry.grid(row=4, column=1)

    tk.Label(root, text="Reconciled").grid(row=5, column=0)
    global reconciled_var
    reconciled_var = tk.BooleanVar()
    reconciled_check = tk.Checkbutton(root, variable=reconciled_var)
    reconciled_check.grid(row=5, column=1)

    tk.Button(root, text="Add Transaction", command=add_transaction_ui).grid(row=6, column=0, columnspan=2)
    
    tk.Button(root, text="Carry Balance to Next Month", command=carry_balance_ui).grid(row=7, column=0, columnspan=2)

    # Create UI elements for generating monthly reports
    tk.Label(root, text="Month").grid(row=8, column=0)
    global month_entry
    month_entry = tk.Entry(root)
    month_entry.grid(row=8, column=1)

    tk.Label(root, text="Year").grid(row=9, column=0)
    global year_entry
    year_entry = tk.Entry(root)
    year_entry.grid(row=9, column=1)

    tk.Button(root, text="Generate Monthly Report", command=generate_report_ui).grid(row=10, column=0, columnspan=2)

    tk.Button(root, text="Export Transactions to CSV", command=export_transactions_ui).grid(row=11, column=0, columnspan=2)


    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()