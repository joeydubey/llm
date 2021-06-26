import argparse
from sys import argv
from order import Order
from orders import get_available_orders, get_order, get_new_order_id
from inout import load, save
from typing import List

def parse_args(args: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest='command')
    
    create_order = subparser.add_parser('create_order')
    list_orders = subparser.add_parser('list_orders')
    take_order = subparser.add_parser('take_order')
    
    create_order.add_argument('origin', type=str)
    create_order.add_argument('destination', type=str)
    
    take_order.add_argument('id', type=int)
    return parser.parse_args(args)

def command(orders: List[Order], file_name: str, args: argparse.Namespace) -> str:

    if not args.command:
        return "No command received. Run \"llm -h\" to see usage."
    
    elif args.command == 'create_order':
        new_order = Order(get_new_order_id(orders), args.origin, args.destination)
        orders.append(new_order)
        save(orders, file_name)
        return f"{getattr(new_order, 'id')}"

    elif args.command == 'list_orders':
        available_orders = get_available_orders(orders)
        return "\n".join(available_orders)
        
    elif args.command == 'take_order':
        if not get_order(orders, args.id):
            return f"Error: order ID {args.id} does not exist."
        else:
            if not getattr(get_order(orders, args.id), "taken"):
                setattr(get_order(orders, args.id), "taken", True)
                save(orders, file_name)
                return ""
            else:
                return f"Order ID {args.id} is already taken. No changes made."

def main():
    file_name = "orders.csv"
    orders = load(file_name)
    orders = sorted(orders)
    output = command(orders, file_name, args = parse_args(argv[1:]))
    if output:
        print(output)

if __name__ == "__main__":
    main()
