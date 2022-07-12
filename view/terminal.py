from tabulate import tabulate
from os import name, system
from clint.textui import colored
import os


def clear():
  if name == 'nt':
    _ = system('cls')


def show_logo():
    filenames = ["logo.txt"]
    clear()
    frames = []
    for name in filenames:
        with open(name, "r", encoding = "utf8") as f:
            frames.append(f.readlines())
        for frame in frames:
            print(colored.green("".join(frame))) 
    print("\n")
    

def print_menu(title, list_options):
    """Prints options in standard menu format like this:

    Main menu:
    (1) Store manager
    (2) Human resources manager
    (3) Inventory manager
    (0) Exit program

    Args:
        title (str): the title of the menu (first row)
        list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)
    """
    option_counter = 0
    show_logo()
    print("\t" + title + "\n")
    for option in list_options:
        print("(" + str(option_counter) + ") " + option)
        option_counter += 1


def print_message(message):
    """Prints a single message to the terminal.

    Args:
        message: str - the message
    """
    print(message)


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """
    print(label + ":" + "\n")
    print(result)


# /--------------------------------\
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \-----------------------------------/
def print_table(table, headers):
    """Prints tabular data like above.

    Args:
        table: list of lists - the table to print out
    """
    print(tabulate(table, headers = headers, tablefmt = "fancy_grid", showindex=True))


def get_input(label):
    value = input(label + "\n")
    return value


def get_inputs(labels):
    """Gets a list of string inputs from the user.

    Args:
        labels: list - the list of the labels to be displayed before each prompt
    """
    pass


def print_error_message(message):
    """Prints an error message to the terminal.

    Args:
        message: str - the error message
    """
    input(colored.red("Error: " + message))

def print_successful_message(message):
    """Prints a green successful message to the terminal.

    Args:
        message: str - the successful message
    """
    input(colored.green("Success: " + message))
