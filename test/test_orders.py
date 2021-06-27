import unittest
from order import Order
from orders import get_all_orders, get_available_orders, get_order, get_new_order_id

#Sample orders to use in testing
o1 = Order(1, "DEL", "BOM", True)
o2 = Order(7, "Hong Kong", "Singapore", False)
o3 = Order(4, "Kennedy Town", "Sheung Wan", False)
test_orders = sorted([o1, o2, o3])

class TestOrders(unittest.TestCase):
    """
    A class used to perform unit testing for the orders module.
    Extends the TestCase class from the unittest module.
    
    Methods
    -------
    test_get_all_orders()
        tests orders.get_all_orders()

    test_get_available_orders()
        tests orders.get_available_orders()

    test_get_order()
        tests orders.get_order()

    test_get_new_order_id()
        tests orders.get_new_order_id()

    """
    def test_get_all_orders(self):
        """
        Tests orders.get_all_orders()
        
        """
        self.assertEqual(get_all_orders([]), [])
        self.assertEqual(get_all_orders([o1]), ["1,DEL,BOM,True"])
        self.assertEqual(get_all_orders(test_orders), ["1,DEL,BOM,True", "4,Kennedy Town,Sheung Wan,False", "7,Hong Kong,Singapore,False"])
    
    def test_get_available_orders(self):
        """
        Tests orders.get_available_orders()
        
        """
        self.assertEqual(get_available_orders([]), [])
        self.assertEqual(get_available_orders([o1]), [])
        self.assertEqual(get_available_orders([o2]), ["7,Hong Kong,Singapore"])
        self.assertEqual(get_available_orders(test_orders), ["4,Kennedy Town,Sheung Wan", "7,Hong Kong,Singapore"])
    
    def test_get_order(self):
        """
        Tests orders.get_order()

        """
        self.assertEqual(get_order(test_orders, 1), o1) #o1 = Order(1, "DEL", "BOM", True)
        self.assertEqual(get_order(test_orders, 7), o2) #o2 = Order(7, "Hong Kong", "Singapore", False)
        self.assertEqual(get_order(test_orders, 4), o3) #o3 = Order(4, "Kennedy Town", "Sheung Wan", False)
    
    def test_get_new_order_id(self):
        """
        Tests orders.get_new_order_id()

        """
        self.assertEqual(get_new_order_id([]), 1) #Empty list -> new order id: 1
        self.assertEqual(get_new_order_id([o1]), 2) #List only contains order id 1 -> new order id: 2
        self.assertEqual(get_new_order_id([o1, o3]), 5) #List contains order ids 1, 4 -> new order id: 5
        self.assertEqual(get_new_order_id(test_orders), 8) #List contains order ids 1, 4, 7 -> new order id: 8


if __name__ == '__main__':
    unittest.main()