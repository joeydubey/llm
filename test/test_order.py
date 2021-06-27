import unittest
from order import Order

#Sample orders to use in testing
o1 = Order(1, "DEL", "BOM", True)
o2 = Order(7, "Hong Kong", "Singapore")
o3 = Order(4, "Kennedy Town", "Sheung Wan")

class TestOrder(unittest.TestCase):
    """
    A class used to performing unit testing on an Order.
    Extends the TestCase class from the unittest module.
    
    Methods
    -------
    test_string_rep()
        tests str(Order)
    
    test_show()
        tests Order.show()
    
    test_get_id()
        tests getter function for Order.id
    
    test_get_origin()
        tests getter function for Order.origin
    
    test_get_destination()
        tests getter function for Order.destination
    
    test_is_taken()
        tests getter function for Order.taken
    
    test_set_taken()
        tests setter function for Order.taken
    
    """
    def test_string_rep(self):
        """
        Tests str(Order).

        """
        self.assertEqual(str(o1), "1,DEL,BOM,True")
        self.assertEqual(str(o2), "7,Hong Kong,Singapore,False")
        self.assertEqual(str(o3), "4,Kennedy Town,Sheung Wan,False")
    
    def test_show(self):
        """
        Tests Order.show().

        """
        self.assertEqual(o1.show(), "1,DEL,BOM")
        self.assertEqual(o2.show(), "7,Hong Kong,Singapore")
        self.assertEqual(o3.show(), "4,Kennedy Town,Sheung Wan")
    
    def test_get_id(self):
        """
        Tests getter function for Order.id

        """
        self.assertEqual(getattr(o1, "id"), 1)
        self.assertEqual(getattr(o2, "id"), 7)
        self.assertEqual(getattr(o3, "id"), 4)
    
    def test_get_origin(self):
        """
        Tests getter function for Order.origin

        """
        self.assertEqual(getattr(o1, "origin"), "DEL")
        self.assertEqual(getattr(o2, "origin"), "Hong Kong")
        self.assertEqual(getattr(o3, "origin"), "Kennedy Town")
    
    def test_get_destination(self):
        """
        Tests getter function for Order.destination

        """
        self.assertEqual(getattr(o1, "destination"), "BOM")
        self.assertEqual(getattr(o2, "destination"), "Singapore")
        self.assertEqual(getattr(o3, "destination"), "Sheung Wan")
    
    def test_is_taken(self):
        """
        Tests getter function for Order.taken

        """
        self.assertEqual(getattr(o1, "taken"), True)
        self.assertEqual(getattr(o2, "taken"), False)
        self.assertEqual(getattr(o3, "taken"), False)
    
    def test_set_taken(self):
        """
        Tests setter function for Order.taken

        """
        temp_o1 = Order(8, "A", "B", True)
        setattr(temp_o1, "taken", False)
        self.assertEqual(getattr(temp_o1, "taken"), False)

        temp_o2 = Order(9, "C", "D")
        setattr(temp_o2, "taken", True)
        self.assertEqual(getattr(temp_o2, "taken"), True)

        temp_o3 = Order(10, "E", "F")
        setattr(temp_o3, "taken", True)
        self.assertEqual(getattr(temp_o3, "taken"), True)

if __name__ == '__main__':
    unittest.main()
