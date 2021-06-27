"""
A module that assists in data persistence across separate runs of the
program by implementing loading orders from and saving orders to disk.

Methods
-------
load(file_name: str) -> List[Order]
    reads all of the orders from the specified file

save(orders: List[Order], file_name: str) -> None
    writes all of the given orders to the specified file

"""

import csv
import ast
from order import Order
from typing import List

def load(file_name: str) -> List[Order]:
    """
    Reads all of the orders from the specified file and makes them available
    to the program.
    The specified file must contain comma separated values,
    with column headings "id", "from", "to" and "taken".
    Returns the list of orders found in the file.

    Parameters
    ----------
    file_name: str
        the name of the file to be read
    
    Raises
    ------
    IOError
        if the file cannot be read
    
    KeyError
        if the column headings cannot be read
    
    Returns
    -------
    orders: List[Order]
        the list of orders read from the file
        
    """
    orders = []
    try: #try to open file to read
        with open(file_name, 'r') as file:
            reader = csv.DictReader(file)
            try: #try to read column headings
                for row in reader:
                    id = ast.literal_eval(row['id']) #evaluate as integer instead of string
                    taken = ast.literal_eval(row['taken']) #evaluate as bool instead of string
                    order = Order(id, row["from"], row["to"], taken)
                    orders.append(order)
            except KeyError: #could not read column headings
                print(f"Error: could not read file: \"{file_name}\".")
                print("Unable to read column headings.")
                print(f"Overwriting the required file \"{file_name}\" for future runs")
                print("with correct column headings: (id, from, to, taken).")
                save(orders, file_name)

    except IOError: #could not read file
        print(f"Error: could not read file: \"{file_name}\".")
        print(f"Creating the required file \"{file_name}\" for future runs.")
        save(orders, file_name)
    
    return orders

def save(orders: List[Order], file_name: str) -> None:
    """
    Writes all of the given orders to the specified file.
    The specified file will contain comma separated values,
    with column headings "id", "from", "to" and "taken".
    
    Parameters
    ----------
    orders: List[Order]
        the list of orders to be written to the file
    
    file_name: str
        the name of the file to be written
    
    Raises
    ------
    IOError
        if the file cannot be written
    
    """
    try:
        with open(file_name, 'w') as file:
            file.write("id,from,to,taken\n") #write column headings
            for order in orders:
                file.write(f"{order}\n")
    except IOError: #could not write file
        print(f"Error: could not write file: \"{file_name}\".")