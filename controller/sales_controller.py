import sys
import datetime as dt
sys.path.append('./')
from model.sales import sales
from controller import data_validator
from view import terminal as view

TRANSACTION_ID_POSITION = 0
CUSTOMER_POSITION = 1
PRODUCT_POSITION = 2
PRICE_POSITION = 3
DATE_POSITION = 4



def list_transactions():
    view.show_logo()
    transactions = sales.get_transactions()
    view.print_table(transactions, sales.HEADERS)
    view.print_successful_message("Transactions have been listed.")


def get_add_transaction_data():
    view.show_logo()
    price_verification = True
    date_verification = True
    customer = view.get_input("Please enter customer:")
    product = view.get_input("Please enter product's name:")
    while price_verification:
        price = view.get_input("Please enter price:")
        price_verification = data_validator.check_price_validation(price)
    while date_verification:
        transaction_date = view.get_input("Please enter transaction's date:")
        date_verification = data_validator.check_date_validation(transaction_date)
    add_transaction(customer, product, price, transaction_date)


def add_transaction(customer, product, price, transaction_date):
    sales.save_new_transaction(customer, product, price, transaction_date)
    view.print_successful_message("Transaction has been added.")


def check_if_transaction_found(transaction_id):
    transactions = sales.get_transactions()
    transaction_found = False
    for line in transactions:
        if line[TRANSACTION_ID_POSITION] == transaction_id:
            transaction_found = True
    return transaction_found


def get_update_transaction_data():
    view.show_logo()
    price_verification = True
    date_verification = True
    transaction_id = view.get_input("Please enter transaction ID for transaction you want to update.")
    transaction_found = check_if_transaction_found(transaction_id)
    if transaction_found:
        customer = view.get_input("Please enter customer:")
        product = view.get_input("Please enter product's name:")
        while price_verification:
            price = view.get_input("Please enter price:")
            price_verification = data_validator.check_price_validation(price)
        while date_verification:
            transaction_date = view.get_input("Please enter transaction's date:")
            date_verification = data_validator.check_date_validation(transaction_date)
        update_transaction(transaction_id, customer, product, price, transaction_date)
        view.print_successful_message("Transaction has been updated.")
    else:
        view.print_error_message("Transaction with that ID has not been found.")


def update_transaction(transaction_id, customer, product, price, date):
    transactions = sales.get_transactions()
    for line in transactions:
        if line[TRANSACTION_ID_POSITION] == transaction_id:
            line[CUSTOMER_POSITION] = customer
            line[PRODUCT_POSITION] = product
            line[PRICE_POSITION] = price
            line[DATE_POSITION] = date
    sales.update_file(transactions)


def get_delete_transaction_data():
    view.show_logo()
    transaction_id = view.get_input("Please enter ID for transaction you want to delete:")
    transaction_found = check_if_transaction_found(transaction_id)
    if transaction_found:
        delete_transaction(transaction_id)
        view.print_successful_message("Transaction has been deleted.")
    else:
        view.print_error_message("Transaction with that ID was not found.")


def delete_transaction(transaction_id):
    transactions = sales.get_transactions()
    for line in transactions:
        if line[TRANSACTION_ID_POSITION] == transaction_id:
            line.clear()
    sales.update_file(transactions)


def show_biggest_revenue_transaction():
    view.show_logo()
    biggest_revenue_transaction = [find_biggest_revenue_transaction()]
    view.print_message("Transaction with the biggest revenue is")
    view.print_table(biggest_revenue_transaction, sales.HEADERS)
    view.print_successful_message("Transaction has been viewed.")


def find_biggest_revenue_transaction():
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


def show_biggest_revenue_product():
    view.show_logo()
    biggest_revenue_product = find_biggest_revenue_product()
    view.print_general_results(biggest_revenue_product, "Product with the biggest revenue is")
    view.print_successful_message("Product has been viewed.")


def find_biggest_revenue_product():
    transactions = sales.get_transactions()
    all_products = set()
    revenue = 0.0
    for line in transactions:
        all_products.add(line[PRODUCT_POSITION])
    products_and_incomes = {product: revenue for product in all_products}
    for product in products_and_incomes:
        for line in transactions:
            if line[PRODUCT_POSITION] == product:
                revenue = revenue + float(line[PRICE_POSITION])
                products_and_incomes[product] = revenue
        revenue = 0.0
    biggest_revenue_product = max(products_and_incomes, key=lambda revenue: products_and_incomes[revenue])
    return biggest_revenue_product


def get_transactions_between_data():
    check_date = True
    while check_date:
        start_date = view.get_input("Please enter first date")
        check_date = data_validator.check_date_validation(start_date)
    check_date = True
    while check_date:
        end_date = view.get_input("Please enter second date")
        check_date = data_validator.check_date_validation(end_date)
    return start_date, end_date


def show_transactions_between():
    view.show_logo()
    start_date, end_date = get_transactions_between_data()
    number_of_transactions = count_transactions_between(start_date, end_date)
    view.print_general_results(number_of_transactions, "\nNumber of transactions between given dates")
    filtered_transactions = find_transactions_between(start_date, end_date)
    view.print_table(filtered_transactions, sales.HEADERS)
    view.print_successful_message("Transactions between given dates have been viewed.")

def count_transactions_between(start_date, end_date):
    """ Args:
        Available string input format: YYYY-MM-DD
        Returns:
        Number of transactions between two given dates
    """
    transactions = find_transactions_between(start_date, end_date)
    return len(transactions)


def find_transactions_between(start_date, end_date):
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


def show_sum_transactions_between():
    view.show_logo()
    start_date, end_date = get_transactions_between_data()
    sum_of_transactions = sum_transactions_between(start_date, end_date)
    view.print_general_results(sum_of_transactions, "Sum of transactions between given dates is")
    view.print_successful_message("Sum of transactions has been viewed.")

def sum_transactions_between(start_date, end_date):
    """ Args:
        Available string input format: YYYY-MM-DD
        Returns:
        Sum of transactions in float format
    """
    filtered_transactions = find_transactions_between(start_date, end_date)
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
        get_add_transaction_data()
    elif option == 3:
        get_update_transaction_data()
    elif option == 4:
        get_delete_transaction_data()
    elif option == 5:
        show_biggest_revenue_transaction()
    elif option == 6:
        show_biggest_revenue_product()
    elif option == 7:
        show_transactions_between()
    elif option == 8:
        show_sum_transactions_between()
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
