import csv
import ast
from order import Order
from typing import List

def load(file_name: str) -> List[Order]:
    orders = []
    try:
        with open(file_name, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                id = ast.literal_eval(row['id'])
                taken = ast.literal_eval(row['taken'])
                order = Order(id, row["from"], row["to"], taken)
                orders.append(order)

    except IOError:
        print(f"Error: could not read file: \"{file_name}\".")
        print(f"Creating the required file \"{file_name}\" for future runs.")
        with open(file_name, 'w') as file:
            file.write("id,from,to,taken\n")
    
    return orders

def save(orders: list[Order], file_name: str) -> None:
    with open(file_name, 'w') as file:
        file.write("id,from,to,taken\n")
        for order in orders:
            file.write(f"{order}\n")