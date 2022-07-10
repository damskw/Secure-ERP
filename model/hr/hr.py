""" Human resources (HR) module

Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""

from model import data_manager, util

DATAFILE = "model/hr/hr.csv"
HEADERS = ["Employee ID", "Name", "Date of birth", "Department", "Clearance"]


def get_all_employees():
    all_employees = data_manager.read_table_from_file(DATAFILE, separator=";")
    return all_employees


def add_new_employee(employee_name, employee_date_of_birth, employee_department, employee_clearance):
    employees = get_all_employees()
    new_employee = []
    employee_id = util.generate_id()
    new_employee.append(employee_id)
    new_employee.append(employee_name)
    new_employee.append(employee_date_of_birth)
    new_employee.append(employee_department)
    new_employee.append(employee_clearance)
    employees.append(new_employee)
    data_manager.write_table_to_file(DATAFILE, employees, separator=";")
    


def update_file(updated_employees):
    data_manager.write_table_to_file(DATAFILE, updated_employees, separator=";")
