import sys
sys.path.append('./')
from model.sales import sales
from view import terminal as view

TRANSACTION_ID_POSITION = 0
CUSTOMER_POSITION = 1
PRODUCT_POSITION = 2
PRICE_POSITION = 3
DATE_POSITION = 4

def list_transactions():
    transactions = sales.get_transactions()
    view.print_table(transactions)


def add_transaction(transaction_id, customer, product, price, date):
    transactions = sales.get_transactions()
    new_transaction = [transaction_id, customer, product, price, date]
    transactions.append(new_transaction)
    sales.update_transactions(transactions)


def update_transaction(transaction_id, customer, product, price, date):
    transactions = sales.get_transactions()
    for line in transactions:
        if line[TRANSACTION_ID_POSITION] == transaction_id:
            line[CUSTOMER_POSITION] = customer
            line[PRODUCT_POSITION] = product
            line[PRICE_POSITION] = price
            line[DATE_POSITION] = date
    sales.update_transactions(transactions)


def delete_transaction(transaction_id):
    transactions = sales.get_transactions()
    delete_all = 0
    for line in transactions:
        if line[TRANSACTION_ID_POSITION] == transaction_id:
            for length in range(len(line)):
                del line[delete_all]
    sales.update_transactions(transactions)


def get_biggest_revenue_transaction():
    view.print_error_message("Not implemented yet.")


def get_biggest_revenue_product():
    view.print_error_message("Not implemented yet.")


def count_transactions_between():
    view.print_error_message("Not implemented yet.")


def sum_transactions_between():
    view.print_error_message("Not implemented yet.")


def run_operation(option):
    if option == 1:
        list_transactions()
    elif option == 2:
        add_transaction()
    elif option == 3:
        update_transaction()
    elif option == 4:
        delete_transaction()
    elif option == 5:
        get_biggest_revenue_transaction()
    elif option == 6:
        get_biggest_revenue_product()
    elif option == 7:
        count_transactions_between()
    elif option == 8:
        sum_transactions_between()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List transactions",
               "Add new transaction",
               "Update transaction",
               "Remove transaction",
               "Get the transaction that made the biggest revenue",
               "Get the product that made the biggest revenue altogether",
               "Count number of transactions between",
               "Sum the price of transactions between"]
    view.print_menu("Sales", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
