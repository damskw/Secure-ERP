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

def update_file(new_transactions):
    data_manager.write_table_to_file(DATAFILE, new_transactions, separator=";")