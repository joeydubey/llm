import unittest
#from order import Order
from code import order

o1 = order.Order(1, "DEL", "BOM", True)
o2 = order.Order(7, "Hong Kong", "Singapore", False)
o3 = order.Order(4, "Kennedy Town", "Sheung Wan", False)

class TestOrder(unittest.TestCase):
    def test_string_rep(self):
        self.assertEqual(str(o1), "1,DEL,BOM,True")
        self.assertEqual(str(o2), "7,Hong Kong,Singapore,False")
        self.assertEqual(str(o3), "4,Kennedy Town,Sheung Wan,False")
    
    def test_get_id(self):
        self.assertEqual(o1.get_id(), 1)
        self.assertEqual(o2.get_id(), 7)
        self.assertEqual(o3.get_id(), 4)
    
    def test_is_taken(self):
        self.assertEqual(o1.is_taken(), True)
        self.assertEqual(o2.is_taken(), False)
        self.assertEqual(o3.is_taken(), False)
    
    def test_show(self):
        self.assertEqual(o1.show(), "1,DEL,BOM")
        self.assertEqual(o2.show(), "7,Hong Kong,Singapore")
        self.assertEqual(o3.show(), "4,Kennedy Town,Sheung Wan")

if __name__ == '__main__':
    unittest.main()
