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


def get_customers():
    all_data = data_manager.read_table_from_file(DATAFILE, separator=";")
    customers = []
    customer_position = 2
    for line in all_data:
        customers.append(line[customer_position])
    return customers