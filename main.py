import argparse
from order import Order
from orders import show_available_orders, exists, get_order, get_new_order_id
from inout import load, save

orders = load("orders.csv")
orders = sorted(orders)

parser = argparse.ArgumentParser()
subparser = parser.add_subparsers(dest='command')

create_order = subparser.add_parser('create_order')
list_orders = subparser.add_parser('list_orders')
take_order = subparser.add_parser('take_order')

create_order.add_argument('origin', type=str)
create_order.add_argument('destination', type=str)

take_order.add_argument('id', type=int)

args = parser.parse_args()

if args.command == 'create_order':
    new_order = Order(get_new_order_id(orders), args.origin, args.destination, False)
    orders.append(new_order)
    save("orders.csv", orders)
    print(new_order.get_id())

elif args.command == 'list_orders':
    show_available_orders(orders)
    
elif args.command == 'take_order':
    if not exists(orders, args.id):
        print("order does not exist")
    else:
        if not get_order(orders, args.id).is_taken():
            get_order(orders, args.id).take()
            save("orders.csv", orders)
        else:
            print("order already taken")