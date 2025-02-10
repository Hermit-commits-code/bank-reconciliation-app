import tkinter as tk
from tkinter import messagebox
from utils.helpers import add_transaction, carry_balance_to_next_month, generate_monthly_report, export_transactions_to_csv, generate_yearly_report, reconcile_transaction

def add_transaction_ui(spreadsheet_path, date_entry, description_entry, transaction_entry, debit_entry, credit_entry):
    date = date_entry.get()
    description = description_entry.get()
    transaction = transaction_entry.get()
    debit = float(debit_entry.get()) if debit_entry.get() else 0.0
    credit = float(credit_entry.get()) if credit_entry.get() else 0.0
    add_transaction(spreadsheet_path, date, description, transaction, debit, credit)
    messagebox.showinfo("Success", "Transaction added successfully!")

def carry_balance_ui(spreadsheet_path):
    carry_balance_to_next_month(spreadsheet_path)
    messagebox.showinfo("Success", "Balance carried to the next month successfully!")

def generate_report_ui(spreadsheet_path, month_entry, year_entry):
    month = int(month_entry.get())
    year = int(year_entry.get())
    generate_monthly_report(spreadsheet_path, month, year)
    messagebox.showinfo("Success", f"Monthly report for {month}/{year} generated successfully!")

def export_transactions_ui(spreadsheet_path):
    export_transactions_to_csv(spreadsheet_path)
    messagebox.showinfo("Success", "Transactions exported to CSV successfully!")

def generate_yearly_report_ui(spreadsheet_path, year_entry):
    year = int(year_entry.get())
    generate_yearly_report(spreadsheet_path, year)
    messagebox.showinfo("Success", f"Yearly report for {year} generated successfully!")

def reconcile_transaction_ui(spreadsheet_path, transaction_entry):
    transaction_id = transaction_entry.get()
    reconcile_transaction(spreadsheet_path, transaction_id)
    messagebox.showinfo("Success", f"Transaction {transaction_id} reconciled successfully!")