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


def get_customers_id():
    all_data = data_manager.read_table_from_file(DATAFILE, separator=";")
    customers_id = []
    customer_id_position = 1
    for line in all_data:
        customers_id.append(line[customer_id_position])
    return customers_id

def get_transactions():
    all_data = data_manager.read_table_from_file(DATAFILE, separator=";")
    transactions = []
    for line in all_data:
        transactions.append(line)
    return transactions