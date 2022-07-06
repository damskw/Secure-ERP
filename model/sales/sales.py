""" Sales module

Data table structure:
    - id (string)
    - customer id (string)
    - product (string)
    - price (float)
    - transaction date (string): in ISO 8601 format (like 1989-03-21)
"""

import sys
sys.path.append('./')
from model import data_manager, util

DATAFILE = "model/sales/sales.csv"
HEADERS = ["Id", "Customer", "Product", "Price", "Date"]


def get_transactions():
    transactions = data_manager.read_table_from_file(DATAFILE, separator=";")
    return transactions


def save_new_transaction(customer, product, price, date):
    transactions = get_transactions()
    new_transaction = []
    transaction_id = util.generate_id()
    new_transaction.append(transaction_id)
    new_transaction.append(customer)
    new_transaction.append(product)
    new_transaction.append(price)
    new_transaction.append(date)
    transactions.append(new_transaction)
    data_manager.write_table_to_file(DATAFILE, transactions, separator=";")

def update_file(updated_transactions):
    data_manager.write_table_to_file(DATAFILE, updated_transactions, separator=";")