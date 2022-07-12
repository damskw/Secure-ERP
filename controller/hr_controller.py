import sys
import datetime as dt
sys.path.append('./')
from model.hr import hr
from view import terminal as view
from dateutil.relativedelta import relativedelta
import string

EMPLOYEE_ID_POSITION = 0
EMPLOYEE_NAME_POSITION = 1
EMPLOYEE_DATE_OF_BIRTH_POSITION = 2
EMPLOYEE_DEPARTMENT_POSITION = 3
EMPLOYEE_CLEARANCE_POSITION = 4


def list_employees():
    view.clear()
    employees = hr.get_all_employees()
    view.print_table(employees, hr.HEADERS)
    view.print_successful_message("Employees have been listed.")


def check_date_validation(date):
    date_of_birth_available_chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-"]
    month_first_char_available = ["0", "1"]
    month_second_char_available = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    day_first_char_available = ["0", "1", "2", "3"]
    day_second_char_available = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    year_char_available = ["1", "2"]
    special_date_character = "-"
    first_special_character_position = 4
    second_special_character_position = 7
    first_char_of_year_position = 0
    first_char_of_month_position = 5
    second_char_of_month_position = 6
    first_char_of_day_position = 8
    second_char_of_day_position = 9
    date_length = 10
    check_date = True
    while check_date:
        if len(date) == date_length:
            for char in date:
                if char not in date_of_birth_available_chars:
                    view.print_error_message("Incorrect data, not allowed characters used.")
                    return True
            if date[first_special_character_position] != special_date_character or date[second_special_character_position] != special_date_character:
                view.print_error_message("Incorrect special sign.")
                return True
            elif date[first_char_of_year_position] not in year_char_available:
                view.print_error_message("Incorrect year.")
                return True
            elif date[first_char_of_month_position] not in month_first_char_available or date[second_char_of_month_position] not in month_second_char_available:
                view.print_error_message("Incorrect month.")
                return True
            elif date[first_char_of_day_position] not in day_first_char_available or date[second_char_of_day_position] not in day_second_char_available:
                view.print_error_message("Incorrect day.")
                return True
            return False
        else:
            view.print_error_message("Incorrect data, invalid length of date.")
            return True


def check_clearance_level_validation(clearance):
    clearance_allowed_characters = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if clearance not in clearance_allowed_characters:
        view.print_error_message("Incorrect clearance level.")
        return True
    return False


def check_department_validation(department):
    available_characters = string.ascii_letters
    for char in department:
        if char not in available_characters:
            view.print_error_message("Department can only be A-Z characters.")
            return True
    return False


def check_name_validation(name):
    available_characters = string.ascii_letters + " "
    for char in name:
        if char not in available_characters:
            view.print_error_message("Name can only be A-Z characters.")
            return True
    return False


def get_add_employee_data():
    view.clear()
    date_verification = True
    clearance_verification = True
    department_check = True
    name_check = True
    while name_check:
        employee_name = view.get_input("Please enter employee name:")
        name_check = check_name_validation(employee_name)
    while date_verification:
        employee_date_of_birth = view.get_input("Please enter date of birth: (YYYY-MM-DD)")
        date_verification = check_date_validation(employee_date_of_birth)
    while department_check:
        employee_department = view.get_input("Please enter name of department:")
        department_check = check_department_validation(employee_department)
    while clearance_verification:
        employee_clearance = view.get_input("Please enter clearance level:")
        clearance_verification = check_clearance_level_validation(employee_clearance)
    add_employee(employee_name, employee_date_of_birth, employee_department, employee_clearance)


def add_employee(employee_name, employee_date_of_birth, employee_department, employee_clearance):
    hr.add_new_employee(employee_name, employee_date_of_birth, employee_department, employee_clearance)
    view.print_successful_message("Employee has been added.")


def get_update_employee_data():
    view.clear()
    date_verification = True
    clearance_verification = True
    department_check = True
    name_check = True
    employee_id = view.get_input("Please enter ID for employee you want to update:")
    employee_found = check_if_employee_found(employee_id)
    if employee_found:
        while name_check:
            employee_name = view.get_input("Please enter employee name:")
            name_check = check_name_validation(employee_name)
        while date_verification:
            employee_date_of_birth = view.get_input("Please enter date of birth: (YYYY-MM-DD)")
            date_verification = check_date_validation(employee_date_of_birth)
        while department_check:
            employee_department = view.get_input("Please enter name of department:")
            department_check = check_department_validation(employee_department)
        while clearance_verification:
            employee_clearance = view.get_input("Please enter clearance level:")
            clearance_verification = check_clearance_level_validation(employee_clearance)
        update_employee(employee_id, employee_name, employee_date_of_birth, employee_department, employee_clearance)
        view.print_successful_message("Employee has been updated.")
    else:
        view.print_error_message("Employee with that ID has not been found.")


def update_employee(employee_id, employee_name, employee_date_of_birth, employee_department, employee_clearance):
    employees = hr.get_all_employees()
    for line in employees:
        if line[EMPLOYEE_ID_POSITION] == employee_id:
            line[EMPLOYEE_NAME_POSITION] = employee_name
            line[EMPLOYEE_DATE_OF_BIRTH_POSITION] = employee_date_of_birth
            line[EMPLOYEE_DEPARTMENT_POSITION] = employee_department
            line[EMPLOYEE_CLEARANCE_POSITION] = employee_clearance
    hr.update_file(employees)


def get_delete_employee_data():
    view.clear()
    employee_id = view.get_input("Please enter ID for employee you want to delete:")
    employee_found = check_if_employee_found(employee_id)
    if employee_found:
        delete_employee(employee_id)
        view.print_successful_message("Employee has been deleted.")
    else:
        view.print_error_message("Employee with that ID was not found")


def delete_employee(employee_id):
    employees = hr.get_all_employees()
    for line in employees:
        if line[EMPLOYEE_ID_POSITION] == employee_id:
            line.clear() 
    hr.update_file(employees)


def check_if_employee_found(employee_id):
    employees = hr.get_all_employees()
    employee_found = False
    for line in employees:
        if line[EMPLOYEE_ID_POSITION] == employee_id:
            employee_found = True 
    return employee_found


def get_oldest_and_youngest():
    first_value = 0
    last_value = -1
    employees = hr.get_all_employees()
    all_ages = []
    date_today = dt.datetime.today()
    for line in employees:
        date_to_compare = dt.datetime.strptime(line[EMPLOYEE_DATE_OF_BIRTH_POSITION], "%Y-%m-%d")
        age = date_today - date_to_compare
        all_ages.append(age)
    all_ages.sort(reverse=True)
    oldest = all_ages[first_value]
    youngest = all_ages[last_value]
    for line in employees:
        date_to_compare = dt.datetime.strptime(line[EMPLOYEE_DATE_OF_BIRTH_POSITION], "%Y-%m-%d")
        if date_today - date_to_compare == oldest:
            oldest_name = line[EMPLOYEE_NAME_POSITION]
            oldest = relativedelta(date_today, date_to_compare).years
        elif date_today - date_to_compare == youngest:
            youngest_name = line[EMPLOYEE_NAME_POSITION]
            youngest = relativedelta(date_today, date_to_compare).years

    return oldest, oldest_name, youngest, youngest_name


def show_oldest_and_youngest():
    view.clear()
    oldest, oldest_name, youngest, youngest_name = get_oldest_and_youngest()
    oldest_and_youngest = {oldest_name: oldest, youngest_name: youngest}
    view.print_general_results(oldest_and_youngest, "Oldest (name: age), youngest (name: age)")
    view.print_successful_message("Oldest and youngest have been viewed.")


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


def show_average_age():
    view.clear()
    average_age = get_average_age()
    view.print_general_results(average_age, "Average age of employees")
    view.print_successful_message("Average age has been viewed.")


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
        return None, None


def get_next_birthday_data():
    view.clear()
    check_date = True
    while check_date:
        date = view.get_input("Please enter date to check birthdays for 2 weeks after that. (YYYY-MM-DD)")
        check_date = check_date_validation(date)
    return date


def show_next_birthdays():
    view.clear()
    date = get_next_birthday_data()
    upcoming_birthdays, upcoming_birthdays_names = next_birthdays(date)
    following_birthdays = {"Names": upcoming_birthdays_names, "Birthdates": upcoming_birthdays}
    if upcoming_birthdays != None:
        view.print_general_results(following_birthdays, "Following birthdays (Name: birthday)")
        view.print_successful_message("Next birthdays have been viewed.")
    else:
        view.print_error_message("No birthdays have been found.")


def count_employees_with_clearance(clearance):
    employees = hr.get_all_employees()
    employee_counter = 0
    for line in employees:
        if line[EMPLOYEE_CLEARANCE_POSITION] == clearance:
            employee_counter += 1
    return employee_counter


def get_employees_with_clearance_data():
    view.clear()
    clearance_check = True
    while clearance_check:
        clearance = view.get_input("Please enter clearance level")
        clearance_check = check_clearance_level_validation(clearance)
    return clearance


def show_employees_with_clearance():
    view.clear()
    clearance = get_employees_with_clearance_data()
    number_of_employees = count_employees_with_clearance(clearance)
    view.print_general_results(number_of_employees, "Employees with provided clearance level")
    view.print_successful_message("Number of employees has been viewed.")


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


def show_employees_per_department():
    view.clear()
    employees_per_department = count_employees_per_department()
    view.print_general_results(employees_per_department, "Employees per department")
    view.print_successful_message("Employees per department have been listed.")


def run_operation(option):
    if option == 1:
        list_employees()
    elif option == 2:
        get_add_employee_data()
    elif option == 3:
        get_update_employee_data()
    elif option == 4:
        get_delete_employee_data()
    elif option == 5:
        show_oldest_and_youngest()
    elif option == 6:
        show_average_age()
    elif option == 7:
        show_next_birthdays()
    elif option == 8:
        show_employees_with_clearance()
    elif option == 9:
        show_employees_per_department()
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
