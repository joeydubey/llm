from .order import Order

def get_all_orders(orders):
    #for order in orders:
    #    print(order)
    return [str(order) for order in orders]

def get_available_orders(orders):
    #for order in orders:
    #    if not order.is_taken():
    #        #print(order.show())
    #        return []
    return [order.show() for order in orders if not order.is_taken()]

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
    return (1 + sorted(orders)[-1].get_id())