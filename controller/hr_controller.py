import sys
import datetime as dt
sys.path.append('./')
from model.hr import hr
from view import terminal as view
from dateutil.relativedelta import relativedelta

EMPLOYEE_ID_POSITION = 0
EMPLOYEE_NAME_POSITION = 1
EMPLOYEE_DATE_OF_BIRTH_POSITION = 2
EMPLOYEE_DEPARTMENT_POSITION = 3
EMPLOYEE_CLEARANCE_POSITION = 4


def list_employees():
    employees = hr.get_all_employees()
    view.print_table(employees, hr.HEADERS)


def add_employee(employee_name, employee_date_of_birth, employee_department, employee_clearance):
    hr.add_new_employee(employee_name, employee_date_of_birth, employee_department, employee_clearance)


def update_employee(employee_id, employee_name, employee_date_of_birth, employee_department, employee_clearance):
    employees = hr.get_all_employees()
    for line in employees:
        if line[EMPLOYEE_ID_POSITION] == employee_id:
            line[EMPLOYEE_NAME_POSITION] = employee_name
            line[EMPLOYEE_DATE_OF_BIRTH_POSITION] = employee_date_of_birth
            line[EMPLOYEE_DEPARTMENT_POSITION] = employee_department
            line[EMPLOYEE_CLEARANCE_POSITION] = employee_clearance
    hr.update_file(employees)


def delete_employee(employee_id):
    employees = hr.get_all_employees()
    for line in employees:
        if line[EMPLOYEE_ID_POSITION] == employee_id:
            line.clear()
    hr.update_file(employees)


def get_oldest_and_youngest():
    employees = hr.get_all_employees()
    all_ages = []
    date_today = dt.datetime.today()
    for line in employees:
        date_to_compare = dt.datetime.strptime(line[EMPLOYEE_DATE_OF_BIRTH_POSITION], "%Y-%m-%d")
        age = date_today - date_to_compare
        all_ages.append(age)
    all_ages.sort(reverse=True)
    oldest = all_ages[0]
    youngest = all_ages[-1]
    for line in employees:
        date_to_compare = dt.datetime.strptime(line[EMPLOYEE_DATE_OF_BIRTH_POSITION], "%Y-%m-%d")
        if date_today - date_to_compare == oldest:
            oldest_name = line[EMPLOYEE_NAME_POSITION]
            oldest = relativedelta(date_today, date_to_compare).years
        elif date_today - date_to_compare == youngest:
            youngest_name = line[EMPLOYEE_NAME_POSITION]
            youngest = relativedelta(date_today, date_to_compare).years

    return oldest, oldest_name, youngest, youngest_name


def count_average(numbers):
    return sum(numbers) // len(numbers)


def get_average_age():
    employees = hr.get_all_employees()
    all_ages = []
    date_today = dt.datetime.today()
    for line in employees:
        date_to_compare = dt.datetime.strptime(line[EMPLOYEE_DATE_OF_BIRTH_POSITION], "%Y-%m-%d")
        age = relativedelta(date_today, date_to_compare).years
        all_ages.append(age)
    average_age = count_average(all_ages)
    return average_age


def change_birthdate_year_for_current(date, given_date):
    future_date_of_birth = date.split("-")
    year_to_change = str(given_date)
    year_to_change = year_to_change[0:4]
    future_date_of_birth[0] = year_to_change
    future_date_of_birth = "-".join(future_date_of_birth)
    future_date_of_birth = dt.datetime.strptime(future_date_of_birth, "%Y-%m-%d")
    return future_date_of_birth


def next_birthdays(given_date):
    employees = hr.get_all_employees()
    number_of_days = 14
    given_date = dt.datetime.strptime(given_date, "%Y-%m-%d")
    date_difference = dt.timedelta(days = number_of_days)
    future_date = given_date + date_difference
    upcoming_birthdays = []
    upcoming_birthdays_names = []
    for line in employees:
        employee_birthdate = line[EMPLOYEE_DATE_OF_BIRTH_POSITION]
        future_date_of_birth = change_birthdate_year_for_current(employee_birthdate, given_date)
        if future_date_of_birth > given_date and future_date_of_birth < future_date:
            upcoming_birthdays.append(employee_birthdate)
    for line in employees:
        for dates in range(len(upcoming_birthdays)):
            if line[EMPLOYEE_DATE_OF_BIRTH_POSITION] == upcoming_birthdays[dates]:
                upcoming_birthdays_names.append(line[EMPLOYEE_NAME_POSITION])
    if upcoming_birthdays:
        return upcoming_birthdays, upcoming_birthdays_names
    else:
        return None


def count_employees_with_clearance(clearance):
    employees = hr.get_all_employees()
    employee_counter = 0
    for line in employees:
        if line[EMPLOYEE_CLEARANCE_POSITION] == clearance:
            employee_counter += 1
    return employee_counter


def count_employees_per_department():
    employees = hr.get_all_employees()
    all_departments = set()
    department_counter = 0
    for line in employees:
        all_departments.add(line[EMPLOYEE_DEPARTMENT_POSITION])
    employees_per_department = {department: department_counter for department in all_departments}
    for department in employees_per_department:
        for line in employees:
            if line[EMPLOYEE_DEPARTMENT_POSITION] == department:
                department_counter += 1
                employees_per_department[department] = department_counter
        department_counter = 0
    return employees_per_department


def run_operation(option):
    if option == 1:
        list_employees()
    elif option == 2:
        add_employee()
    elif option == 3:
        update_employee()
    elif option == 4:
        delete_employee()
    elif option == 5:
        get_oldest_and_youngest()
    elif option == 6:
        get_average_age()
    elif option == 7:
        next_birthdays()
    elif option == 8:
        count_employees_with_clearance()
    elif option == 9:
        count_employees_per_department()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List employees",
               "Add new employee",
               "Update employee",
               "Remove employee",
               "Oldest and youngest employees",
               "Employees average age",
               "Employees with birthdays in the next two weeks",
               "Employees with clearance level",
               "Employee numbers by department"]
    view.print_menu("Human resources", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
