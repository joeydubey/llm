import unittest
from io import StringIO
from order import Order
from inout import load
from main import parse_args, command

#o1 = Order(1, "DEL", "BOM", True)
#o2 = Order(7, "Hong Kong", "Singapore", False)
#o3 = Order(4, "Kennedy Town", "Sheung Wan", False)
#orders = [o1, o2, o3]
cmd_empty = ""
cmd_create1 = "create_order Sydney Auckland"
cmd_create2 = "create_order"
cmd_create3 = "create_order Sydney"
cmd_list1 = "list_orders"
cmd_list2 = "list_orders foo"
cmd_take1 = "take_order 7"
cmd_take2 = "take_order a"
cmd_take3 = "take_order"
cmd_take4 = "take_order 7 2"

class TestMain(unittest.TestCase):
    def test_parser_create(self):
        args = parse_args(cmd_create1.split())
        self.assertEqual(args.command, "create_order")
        self.assertEqual(args.origin, "Sydney")
        self.assertEqual(args.destination, "Auckland")

        with self.assertRaises(SystemExit):
            args = parse_args(cmd_create2.split())
        
        with self.assertRaises(SystemExit):
            args = parse_args(cmd_create3.split())
    
    def test_parser_list(self):
        args = parse_args(cmd_list1.split())
        self.assertEqual(args.command, "list_orders")

        with self.assertRaises(SystemExit):
            args = parse_args(cmd_list2.split())
    
    def test_parser_take(self):
        args = parse_args(cmd_take1.split())
        self.assertEqual(args.command, "take_order")
        self.assertEqual(args.id, 7)

        with self.assertRaises(SystemExit):
            args = parse_args(cmd_take2.split())
        
        with self.assertRaises(SystemExit):
            args = parse_args(cmd_take3.split())
        
        with self.assertRaises(SystemExit):
            args = parse_args(cmd_take4.split())
        
    def test_parser_empty(self):
        args = parse_args(cmd_empty.split())
        self.assertEqual(args.command, None)

if __name__ == '__main__':
    unittest.main()
