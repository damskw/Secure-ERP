import sys
import datetime as dt
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
    view.print_table(transactions, sales.HEADERS)


def add_transaction(customer, product, price, date):
    sales.save_new_transaction(customer, product, price, date)



def update_transaction(transaction_id, customer, product, price, date):
    transactions = sales.get_transactions()
    for line in transactions:
        if line[TRANSACTION_ID_POSITION] == transaction_id:
            line[CUSTOMER_POSITION] = customer
            line[PRODUCT_POSITION] = product
            line[PRICE_POSITION] = price
            line[DATE_POSITION] = date
    sales.update_file(transactions)


def delete_transaction(transaction_id):
    transactions = sales.get_transactions()
    for line in transactions:
        if line[TRANSACTION_ID_POSITION] == transaction_id:
            line.clear()
    sales.update_file(transactions)


def get_biggest_revenue_transaction():
    transactions = sales.get_transactions()
    revenues = []
    for line in transactions:
        revenues.append(line[PRICE_POSITION])
    revenues.sort(reverse=True)
    biggest_revenue_value = revenues[0]
    for line in transactions:
        if line[PRICE_POSITION] == biggest_revenue_value:
            biggest_revenue_transaction = line
    return biggest_revenue_transaction

def get_biggest_revenue_product():
    transactions = sales.get_transactions()
    revenues = []
    for line in transactions:
        revenues.append(line[PRICE_POSITION])
    revenues.sort(reverse=True)
    biggest_revenue_value = revenues[0]
    for line in transactions:
        if line[PRICE_POSITION] == biggest_revenue_value:
            biggest_revenue_product = line[PRODUCT_POSITION]
    return biggest_revenue_product


def count_transactions_between(start_date, end_date):
    """ Args:
        Available string input format: YYYY-MM-DD
        Returns:
        Number of transactions between two given dates
    """
    transactions = get_transactions_between(start_date, end_date)
    return len(transactions)


def get_transactions_between(start_date, end_date):
    """ Args:
        Available string input format: YYYY-MM-DD
        Returns:
        List of transactions between two dates
    """
    transactions = sales.get_transactions()
    filtered_transactions = []
    start_date = dt.datetime.strptime(start_date, "%Y-%m-%d")
    end_date = dt.datetime.strptime(end_date, "%Y-%m-%d")
    for line in transactions:
        date_to_compare = dt.datetime.strptime(line[DATE_POSITION], "%Y-%m-%d")
        if date_to_compare >= start_date and date_to_compare <= end_date:
            filtered_transactions.append(line)
    return filtered_transactions
    

def sum_transactions_between(start_date, end_date):
    """ Args:
        Available string input format: YYYY-MM-DD
        Returns:
        Sum of transactions in float format
    """
    filtered_transactions = get_transactions_between(start_date, end_date)
    all_prices = []
    sum_of_transactions = 0.0
    for line in filtered_transactions:
            price = float(line[PRICE_POSITION])
            all_prices.append(price)
    for element in all_prices:
        sum_of_transactions = sum_of_transactions + element
    return sum_of_transactions

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
