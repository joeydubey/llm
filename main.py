"""
Simple Order Manager

This script implements a simple command line interface that allows
the user to create, list and take orders.

For persistent data across multiple runs, the orders are saved to
and loaded from the file "orders.csv" in the program directory.
If the file is not found or cannot be read, the program will generate
this file.

This script can also be imported as a module.

Methods
-------
parse_args(args: List[str]) -> argparse.Namespace
    parses all the input arguments and returns an argparse.Namespace object

command(orders: List[Order], file_name: str, args: argparse.Namespace) -> str
    processes the arguments passed to take appropriate action

main() -> None
    the main function of the script    

"""
import argparse
from sys import argv
from order import Order
from orders import get_available_orders, get_order, get_new_order_id
from inout import load, save
from typing import List

def parse_args(args: List[str]) -> argparse.Namespace:
    """
    Parses all the input arguments received and returns an
    argparse.Namespace type object containing the parsed arguments
    for further handling.

    Parameters
    ----------
    args: List[str]
        the list of strings containing the arguments passed to the program

    Returns
    -------
    parsed_args: argparse.Namespace
        the parsed arguments

    """
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(
        dest='command',
        description="Receive a command from the user and take the appropriate action",
        metavar="[create_orderlist_orders|take_order]\n"
    )
    
    create_order = subparser.add_parser('create_order', help="Create a new order")
    list_orders = subparser.add_parser('list_orders', help="List all available orders")
    take_order = subparser.add_parser('take_order', help="Take an available order")
    
    create_order.add_argument('origin', type=str, help="Where the order is coming from")
    create_order.add_argument('destination', type=str, help="Where the order is going to")
    
    take_order.add_argument('id', type=int, help="Unique id of the order to be taken")
    
    parsed_args=parser.parse_args(args)
    return parsed_args

def command(orders: List[Order], file_name: str, parsed_args: argparse.Namespace) -> str:
    """
    Processes the parsed arguments passed to the program and takes
    appropriate action corresponding to the given command.
    
    If no command is passed, no action is taken.
    
    If "create_order" command is received, a new order is created.
    Throws an error if origin and destination of order are not received.

    If "list_orders" command is received, all the available orders
    are listed.

    If "take_order" command is received, the status of the specified order
    is changed to taken.
    Throws an error if the order does not exist, or if it has already
    been taken.

    Returns a string as output.

    Parameters
    ----------
    orders: List[Order]
        the list of orders to be used by the program

    parsed_args: argparse.Namespace
        the parsed arguments passed to the program

    Returns
    -------
    output: str
        the formatted string output for the given command

    """
    if not parsed_args.command: #No command received
        output = f"Error: no arguments received. Run \"./llm -h\" to see usage."
    
    elif parsed_args.command == 'create_order':
        #generate the new order
        new_order = Order(get_new_order_id(orders), parsed_args.origin, parsed_args.destination)
        orders.append(new_order)
        #save to file for future runs
        save(orders, file_name)
        output = f"{getattr(new_order, 'id')}"

    elif parsed_args.command == 'list_orders':
        #get all the available (untaken) orders
        available_orders = get_available_orders(orders)
        output = "\n".join(available_orders)
        
    elif parsed_args.command == 'take_order':
        if not get_order(orders, parsed_args.id): #order does not exist
            output = f"Error: order ID {parsed_args.id} does not exist."
        else:
            if not getattr(get_order(orders, parsed_args.id), "taken"): #order available
                #change order status to taken
                setattr(get_order(orders, parsed_args.id), "taken", True)
                #save to file for future runs
                save(orders, file_name)
                output = ""
            else: #order already taken
                output = f"Error: order ID {parsed_args.id} is already taken. No changes made."
    
    return output

def main():
    file_name = "orders.csv"

    orders = load(file_name) #load orders from "orders.csv"
    orders = sorted(orders) #sort the orders (by id) for better presentation

    output = command(orders, file_name, parsed_args = parse_args(argv[1:])) #get arguments from command line and take appropriate action
    
    if output: #Non-empty string output
        print(output)

if __name__ == "__main__":
    main()
