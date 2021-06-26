"""
A module that implements helper functions to supplement the Order class

Methods
-------

get_all_orders(orders: List[Order]) -> List[str]
    returns a list of formatted string representations of
    all orders in a list of orders

get_available_orders(orders: List[Order]) -> List[str]
    returns a list of formatted string representations of
    all available orders in a list of orders

get_order(orders: List[Order], id: int) -> Order
    retrieves the order with the specified order "id" from a list of orders

get_new_order_id(orders: List[Order]) -> int
    generates a unique order "id" to allot to a new order being added to a
    list of orders

"""

from order import Order
from typing import List

def get_all_orders(orders: List[Order]) -> List[str]:
    """
    Returns a list of formatted string representations of
    all orders in a given list of orders.

    Parameters
    ----------
    orders: List[Order]
        the list of orders for which string representations are to be generated
    
    """
    return [str(order) for order in orders]

def get_available_orders(orders: List[Order]) -> List[str]:
    """
    Returns a list of formatted string representations of
    all available (untaken) orders in a given list of orders.

    Parameters
    ----------
    orders: List[Order]
        the list of orders for which string representations are to be generated
    
    """
    return [order.show() for order in orders if not getattr(order, "taken")]

def get_order(orders: List[Order], id: int) -> Order:
    """
    Finds the order with a specified order "id" in the given list of orders.
    Returns the order if found, otherwise, returns a NoneType object.

    Parameters
    ----------
    orders: List[Order]
        the list of orders which is to be searched for the specified "id"
    
    id: int
        the order "id" to look for
    
    Returns
    -------
    order: Order
        the order to be retrieved
    
    """
    for order in orders:
        if getattr(order, "id") == id:
            return order

def get_new_order_id(orders: List[Order]) -> int:
    """
    Generates a unique order "id" to allot to a new order being added to a
    the given list of orders.
    Finds the largest order "id" in the list of orders and increments it.
    This guarantees that the generated order "id" is unique for the given list.
    Returns a positive integer. 

    Parameters
    ----------
    orders: List[Order]
        the list of orders for which the new order "id" is to be generated
    
    """
    if not orders: #list of orders is empty
        return 1 #"id" 1 is unique for empty list
    
    #non-empty list
    return (1 + getattr(max(orders), "id")) #"id" 1+(max order "id" in list)