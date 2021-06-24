from order import Order

def show_all_orders(orders):
    for order in orders:
        print(order)

def show_available_orders(orders):
    for order in orders:
        if not order.is_taken():
            print(order.show())

def exists(orders, id):
    dummy_order = Order(id, "", "", False)
    return (dummy_order in orders)

def get_order(orders, id):
    for order in orders:
        if order.get_id() == id:
            return order

def get_new_order_id(orders):
    if not orders:
        return 1
    return (1 + orders[-1].get_id())