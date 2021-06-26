from order import Order
from typing import List

def get_all_orders(orders: List[Order]) -> List[str]:
    #for order in orders:
    #    print(order)
    return [str(order) for order in orders]

def get_available_orders(orders: List[Order]) -> List[str]:
    #for order in orders:
    #    if not order.is_taken():
    #        #print(order.show())
    #        return []
    return [order.show() for order in orders if not order.is_taken()]

def get_order(orders: List[Order], id: int) -> Order:
    for order in orders:
        if getattr(order, "id") == id:
            return order

def get_new_order_id(orders: List[Order]) -> int:
    if not orders:
        return 1 
    return (1 + getattr(max(orders), "id"))