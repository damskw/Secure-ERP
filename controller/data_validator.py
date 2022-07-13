import sys
sys.path.append('./')
from view import terminal as view
import string

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


def check_clearance_level_validation(clearance):
    clearance_allowed_characters = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if clearance not in clearance_allowed_characters:
        view.print_error_message("Incorrect clearance level.")
        return True
    return False


def check_price_validation(price):
    available_characters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
    available_first_position = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    available_last_position = available_first_position + ["0"]
    first_position = 0
    last_position = -1
    for char in price:
        if char not in available_characters:
            view.print_error_message("Price can only be a number.")
            return True
    if price[first_position] not in available_first_position or price[last_position] not in available_last_position:
        view.print_error_message("Invalid price format.")
        return True
    return False


def check_email_validation(email):
    must_be_used_characters = ["@", "."]
    must_be_used_characters_counter = 0
    must_be_used_characters_maximum_value = 2
    for char in email:
        if char in must_be_used_characters:
            must_be_used_characters_counter += 1
    if must_be_used_characters_counter != must_be_used_characters_maximum_value:
        view.print_error_message("Incorrect email.")
        return True
    return False


def check_customer_subscribed_validation(customer_subscribed):
    available_length = 1
    available_characters = ["0", "1"]
    if len(customer_subscribed) == available_length:
        if customer_subscribed in available_characters:
            return False
        else:
            view.print_error_message("Incorrect value.")
            return True
    else:
        view.print_error_message("Incorrect length.")
        return True  