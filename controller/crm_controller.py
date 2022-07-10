import sys
sys.path.append('./')
from model.crm import crm
from view import terminal as view


CUSTOMER_ID_POSITION = 0
CUSTOMER_NAME_POSITION = 1
CUSTOMER_EMAIL_POSITION = 2
CUSTOMER_SUBSCRIBED_POSITION = 3
SUBSCRIBED = "1"
UNSUBSCRIBED = "0"

def list_customers():
    customers = crm.get_all_customers()
    view.print_table(customers, crm.HEADERS)

def add_customer(customer_name, customer_email, customer_subscribed):
    crm.save_new_customer(customer_name, customer_email, customer_subscribed)


def update_customer(customer_id, customer_name, customer_email, customer_subscribed):
    customers = crm.get_all_customers()
    for line in customers:
        if line[CUSTOMER_ID_POSITION] == customer_id:
            line[CUSTOMER_NAME_POSITION] = customer_name
            line[CUSTOMER_EMAIL_POSITION] = customer_email
            line[CUSTOMER_SUBSCRIBED_POSITION] = customer_subscribed
    crm.update_file(customers)


def delete_customer(customer_id):
    customers = crm.get_all_customers()
    for line in customers:
        if line[CUSTOMER_ID_POSITION] == customer_id:
            line.clear()
    crm.update_file(customers)


def get_subscribed_emails():
    customers = crm.get_all_customers()
    subscribed_emails = []
    for line in customers:
        if line[CUSTOMER_SUBSCRIBED_POSITION] == SUBSCRIBED:
            subscribed_emails.append(line[CUSTOMER_EMAIL_POSITION])
    return subscribed_emails


def run_operation(option):
    if option == 1:
        list_customers()
    elif option == 2:
        add_customer()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
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
