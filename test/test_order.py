import unittest
from order import Order

o1 = Order(1, "DEL", "BOM", True)
o2 = Order(7, "Hong Kong", "Singapore")
o3 = Order(4, "Kennedy Town", "Sheung Wan")

class TestOrder(unittest.TestCase):
    def test_string_rep(self):
        self.assertEqual(str(o1), "1,DEL,BOM,True")
        self.assertEqual(str(o2), "7,Hong Kong,Singapore,False")
        self.assertEqual(str(o3), "4,Kennedy Town,Sheung Wan,False")
    
    def test_show(self):
        self.assertEqual(o1.show(), "1,DEL,BOM")
        self.assertEqual(o2.show(), "7,Hong Kong,Singapore")
        self.assertEqual(o3.show(), "4,Kennedy Town,Sheung Wan")
    
    def test_get_id(self):
        self.assertEqual(getattr(o1, "id"), 1)
        self.assertEqual(getattr(o2, "id"), 7)
        self.assertEqual(getattr(o3, "id"), 4)
    
    def test_is_taken(self):
        self.assertEqual(getattr(o1, "taken"), True)
        self.assertEqual(getattr(o2, "taken"), False)
        self.assertEqual(getattr(o3, "taken"), False)
    
    def test_set_taken(self):
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
