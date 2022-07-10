""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""

import sys
sys.path.append('./')
from model import data_manager, util


DATAFILE = "model/crm/crm.csv"
HEADERS = ["Customer ID", "Name", "E-mail", "Subscribed"]


def get_all_customers():
    all_customers = data_manager.read_table_from_file(DATAFILE, separator=";")
    return all_customers

def save_new_customer(name, email, subscribed):
    all_customers = get_all_customers()
    new_customer = []
    customer_id = util.generate_id()
    new_customer.append(customer_id)
    new_customer.append(name)
    new_customer.append(email)
    new_customer.append(subscribed)
    all_customers.append(new_customer)
    data_manager.write_table_to_file(DATAFILE, all_customers, separator = ";")


def update_file(new_crm_data):
    data_manager.write_table_to_file(DATAFILE, new_crm_data, separator=";")