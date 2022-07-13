from distutils.command import check
import sys
sys.path.append('./')
from model.crm import crm
from view import terminal as view
from controller import data_validator


CUSTOMER_ID_POSITION = 0
CUSTOMER_NAME_POSITION = 1
CUSTOMER_EMAIL_POSITION = 2
CUSTOMER_SUBSCRIBED_POSITION = 3
SUBSCRIBED = "1"
UNSUBSCRIBED = "0"

def list_all_customers():
    view.show_logo()
    customers = crm.get_all_customers()
    view.print_table(customers, crm.HEADERS)
    view.print_successful_message("List of customers has been viewed.")


def get_add_customer_data():
    view.show_logo()
    email_check = True
    subscribed_check = True
    customer_name = view.get_input("Please enter customer's name:")
    while email_check:
        customer_email = view.get_input("Please enter e-mail:")
        email_check = data_validator.check_email_validation(customer_email)
    while subscribed_check:
        customer_subscribed = view.get_input("Please enter subscribed status: (0 - no subscription, 1 - subscripton)")
        subscribed_check = data_validator.check_customer_subscribed_validation(customer_subscribed)
    add_customer(customer_name, customer_email, customer_subscribed)
    view.print_successful_message("Customer has been added.")
    


def add_customer(customer_name, customer_email, customer_subscribed):
    crm.save_new_customer(customer_name, customer_email, customer_subscribed)


def check_if_customer_found(customer_id):
    customers = crm.get_all_customers()
    customer_found = False
    for line in customers:
        if line[CUSTOMER_ID_POSITION] == customer_id:
            customer_found = True 
    return customer_found


def get_update_customer_data():
    view.show_logo()
    email_check = True
    subscribed_check = True
    customer_id = view.get_input("Please enter ID for a customer you want to update:")
    customer_found = check_if_customer_found(customer_id)
    if customer_found:
        customer_name = view.get_input("Please enter customer's name:")
        while email_check:
            customer_email = view.get_input("Please enter e-mail:")
            email_check = data_validator.check_email_validation(customer_email)
        while subscribed_check:
            customer_subscribed = view.get_input("Please enter subscribed status: (0 - no subscription, 1 - subscripton)")
            subscribed_check = data_validator.check_customer_subscribed_validation(customer_subscribed)
        update_customer(customer_id, customer_name, customer_email, customer_subscribed)
        view.print_successful_message("Customer has been updated.")
    else:
        view.print_error_message("Customer with that ID has not been found.")


def update_customer(customer_id, customer_name, customer_email, customer_subscribed):
    customers = crm.get_all_customers()
    for line in customers:
        if line[CUSTOMER_ID_POSITION] == customer_id:
            line[CUSTOMER_NAME_POSITION] = customer_name
            line[CUSTOMER_EMAIL_POSITION] = customer_email
            line[CUSTOMER_SUBSCRIBED_POSITION] = customer_subscribed
    crm.update_file(customers)


def get_delete_customer_data():
    view.show_logo()
    customer_id = view.get_input("Please enter ID for customer you want to delete:")
    customer_found = check_if_customer_found(customer_id)
    if customer_found:
        delete_customer(customer_id)
        view.print_successful_message("Customer has been deleted.")
    else:
        view.print_error_message("Customer with that ID was not found")


def delete_customer(customer_id):
    customers = crm.get_all_customers()
    for line in customers:
        if line[CUSTOMER_ID_POSITION] == customer_id:
            line.clear()
    crm.update_file(customers)


def show_subscribed_emails():
    view.show_logo()
    subscribed_emails = get_subscribed_emails()
    view.print_general_results(subscribed_emails, "Subscribed emails are:")
    view.print_successful_message("Emails have been viewed.")


def get_subscribed_emails():
    customers = crm.get_all_customers()
    subscribed_emails = []
    for line in customers:
        if line[CUSTOMER_SUBSCRIBED_POSITION] == SUBSCRIBED:
            subscribed_emails.append(line[CUSTOMER_EMAIL_POSITION])
    return subscribed_emails


def run_operation(option):
    if option == 1:
        list_all_customers()
    elif option == 2:
        get_add_customer_data()
    elif option == 3:
        get_update_customer_data()
    elif option == 4:
        get_delete_customer_data()
    elif option == 5:
        show_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List customers",
               "Add new customer",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails"]
    view.print_menu("Customer Relationship Management", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
