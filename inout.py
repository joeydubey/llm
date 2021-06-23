import csv
import ast
from order import Order

def load(file_name):
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        orders = []
        for row in reader:
            id = ast.literal_eval(row['id'])
            taken = ast.literal_eval(row['taken'])
            order = Order(id, row["from"], row["to"], taken)
            orders.append(order)
    return orders

def save(file_name, orders):
    with open(file_name, 'w') as file:
        file.write("id,from,to,taken\n")
        for order in orders:
            file.write(f"{order}\n")