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
    txn_type = type_entry.get()
    amount = float(amount_entry.get())

    add_transaction(spreadsheet_path, date, description, transaction, txn_type, amount)
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

    tk.Label(root, text="Transaction").grid(row=2, column=0)
    global transaction_entry
    transaction_entry = tk.Entry(root)
    transaction_entry.grid(row=2, column=1)

    tk.Label(root, text="Type (Withdrawal/Deposit)").grid(row=3, column=0)
    global type_entry
    type_entry = tk.Entry(root)
    type_entry.grid(row=3, column=1)

    tk.Label(root, text="Amount").grid(row=4, column=0)
    global amount_entry
    amount_entry = tk.Entry(root)
    amount_entry.grid(row=4, column=1)

    tk.Button(root, text="Add Transaction", command=add_transaction_ui).grid(row=5, column=0, columnspan=2)

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()