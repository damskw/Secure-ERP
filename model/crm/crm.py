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
HEADERS = ["id", "name", "email", "subscribed"]


def get_all_crm_data():
    all_data = data_manager.read_table_from_file(DATAFILE, separator=";")
    return all_data


def update_file(new_crm_data):
    data_manager.write_table_to_file(DATAFILE, new_crm_data, separator=";")