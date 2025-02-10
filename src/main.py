import os
import tkinter as tk
from utils.helpers import create_spreadsheet
from ui import add_transaction_ui, carry_balance_ui, generate_report_ui, export_transactions_ui, generate_yearly_report_ui, reconcile_transaction_ui

def main():
    global spreadsheet_path
    spreadsheet_path = 'data/transactions.xlsx'
    os.makedirs(os.path.dirname(spreadsheet_path), exist_ok=True)
    create_spreadsheet(spreadsheet_path)

    root = tk.Tk()
    root.title("Bank Reconciliation Application")

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

    tk.Button(root, text="Add Transaction", command=lambda: add_transaction_ui(spreadsheet_path, date_entry, description_entry, transaction_entry, debit_entry, credit_entry, reconciled_var)).grid(row=6, column=0, columnspan=2)
    tk.Button(root, text="Carry Balance to Next Month", command=lambda: carry_balance_ui(spreadsheet_path)).grid(row=7, column=0, columnspan=2)

    tk.Label(root, text="Month").grid(row=8, column=0)
    global month_entry
    month_entry = tk.Entry(root)
    month_entry.grid(row=8, column=1)

    tk.Label(root, text="Year").grid(row=9, column=0)
    global year_entry
    year_entry = tk.Entry(root)
    year_entry.grid(row=9, column=1)

    tk.Button(root, text="Generate Monthly Report", command=lambda: generate_report_ui(spreadsheet_path, month_entry, year_entry)).grid(row=10, column=0, columnspan=2)
    tk.Button(root, text="Export Transactions to CSV", command=lambda: export_transactions_ui(spreadsheet_path)).grid(row=11, column=0, columnspan=2)
    tk.Button(root, text="Generate Yearly Report", command=lambda: generate_yearly_report_ui(spreadsheet_path, year_entry)).grid(row=12, column=0, columnspan=2)
    tk.Button(root, text="Reconcile Transaction", command=lambda: reconcile_transaction_ui(spreadsheet_path, transaction_entry)).grid(row=13, column=0, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    main()