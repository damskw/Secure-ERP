# Do not modify this file!
import csv
import pandas as pd

def read_table_from_file(file_name, separator=';'):
    """Read CSV file into a data table.

    Args:
        file_name: The name of the CSV data file.
        separator: The CSV separator character

    Returns:
        The data parsed into a list of lists.
    """
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
        return [element.replace("\n", "").split(separator) for element in lines]
    except IOError:
        return []


def write_table_to_file(file_name, table, separator=';'):
    """Write tabular data into a CSV file.

    Args:
        file_name: The name of the file to write to.
        table: list of lists containing tabular data.
        separator: The CSV separator character
    """
    with open(file_name, "w") as file:
        for record in table:
            row = separator.join(record)
            file.write(row + "\n")
    clear_blank_spaces(file_name)

def clear_blank_spaces(file_name):
    df = pd.read_csv(file_name)
    df.to_csv(file_name, index=False)