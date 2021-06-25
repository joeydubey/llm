import unittest
from io import StringIO
from order import Order
from orders import get_new_order_id
from inout import load, save
from main import parse_args, command

o1 = Order(1, "DEL", "BOM", True)
o2 = Order(7, "Hong Kong", "Singapore", False)
o3 = Order(4, "Kennedy Town", "Sheung Wan", False)
test_orders = sorted([o1, o2, o3])

class TestMain(unittest.TestCase):
    def test_parser_create(self):
        args = parse_args("create_order Sydney Auckland".split())
        self.assertEqual(args.command, "create_order")
        self.assertEqual(args.origin, "Sydney")
        self.assertEqual(args.destination, "Auckland")

        with self.assertRaises(SystemExit):
            args = parse_args("create_order".split())
        
        with self.assertRaises(SystemExit):
            args = parse_args("create_order Sydney".split())
    
    def test_parser_list(self):
        args = parse_args("list_orders".split())
        self.assertEqual(args.command, "list_orders")

        with self.assertRaises(SystemExit):
            args = parse_args("list_orders foo".split())
    
    def test_parser_take(self):
        args = parse_args("take_order 7".split())
        self.assertEqual(args.command, "take_order")
        self.assertEqual(args.id, 7)

        with self.assertRaises(SystemExit):
            args = parse_args("take_order a".split())
        
        with self.assertRaises(SystemExit):
            args = parse_args("take_order".split())
        
        with self.assertRaises(SystemExit):
            args = parse_args("take_order 7 2".split())
        
    def test_parser_empty(self):
        args = parse_args("".split())
        self.assertEqual(args.command, None)

    def test_command_create(self):
        args = parse_args("".split())
        test_output = command(test_orders, "test.csv", args)
        self.assertEqual(test_output, "No command received. Run \"llm -h\" to see usage.")

        args = parse_args("create_order Sydney Auckland".split())
        test_output = command(test_orders, "test.csv", args)
        self.assertEqual(test_output, "8")

        args = parse_args("create_order,Tsing Yi,Tuen Mun".split(",")) #Used "," as a separator in place of " " because origin and destination contain spaces.
        test_output = command(test_orders, "test.csv", args)
        self.assertEqual(test_output, "9")

        args = parse_args("create_order TST Central".split())
        test_output = command(test_orders, "test.csv", args)
        self.assertEqual(test_output, "10")
    
    def test_command_list(self):
        args = parse_args("list_orders".split())
        test_output = command(test_orders, "test.csv", args)
        self.assertEqual(test_output, "".join(
            ["4,Kennedy Town,Sheung Wan\n",
            "7,Hong Kong,Singapore\n",
            "8,Sydney,Auckland\n",
            "9,Tsing Yi,Tuen Mun\n",
            "10,TST,Central"]))
    
    def test_command_take(self):
        args = parse_args("take_order 7".split())
        test_output = command(test_orders, "test.csv", args)
        self.assertEqual(test_output, "")

        args = parse_args("take_order 1".split())
        test_output = command(test_orders, "test.csv", args)
        self.assertEqual(test_output, "Order ID 1 is already taken. No changes made.")

        args = parse_args("take_order 50".split())
        test_output = command(test_orders, "test.csv", args)
        self.assertEqual(test_output, "Error: order ID 50 does not exist.")
    
    def test_command_empty(self):
        args = parse_args("".split())
        test_output = command(test_orders, "test.csv", args)
        self.assertEqual(test_output, "No command received. Run \"llm -h\" to see usage.")


if __name__ == '__main__':
    unittest.main()
