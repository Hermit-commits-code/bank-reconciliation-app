# filepath: bank-reconciliation-app/src/main.py
import os
import tkinter as tk
from tkinter import messagebox
from utils.helpers import create_spreadsheet, add_transaction

def add_transaction_ui():
    """
    Function to add a transaction through the UI.
    """
    date = date_entry.get()
    description = description_entry.get()
    transaction = transaction_entry.get()
    debit = float(debit_entry.get()) if debit_entry.get() else 0.0
    credit = float(credit_entry.get()) if credit_entry.get() else 0.0

    add_transaction(spreadsheet_path, date, description, transaction, debit, credit)
    messagebox.showinfo("Success", "Transaction added successfully!")

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

    tk.Button(root, text="Add Transaction", command=add_transaction_ui).grid(row=5, column=0, columnspan=2)

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()