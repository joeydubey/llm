# Lalamove Fresh Grad Tech Challenge
This is a command line program built for the Lalamove Fresh Grad Coding Challenge.
The program can create/list/take an order, to simulate a very simple Lalamove.

## How
This program has been implemented in Python 3.x due to its ease of development
and wide variety of built-in modules which make implemntation of a CLI, testing
and deployment very simple and efficient.

The orders are saved in a file, `orders.csv`, to allow access across multiple runs.
The `setup.sh` script at the root of the project initializes the file `orders.csv`
if it does not exist, and builds the executable `llm` using the PyInstaller package.

## Build
To build the executable, run `./setup.sh`. It will install the required dependencies
and create the executable `llm` in the program root folder.

## Usage
The program can take the following commands:

`create_order [from] [to]`
Returns a unique ID for this order.
from and to are required arguments.

`list_orders`
Lists all the available (non-taken) orders in the format
`id,from,to`.

`take_order [id]`
Takes the order with the given unique ID.
Displays an error if the order is already taken or if it does not exist.
id is a required argument.

`-h || --help`
Displays a help message describing the program features and usage. 

## Interaction example:
```
$ ./llm create_order "Central" "HKU"
1
$ ./llm create_order "Kennedy Town" "Discovery Bay"
2
$ ./llm list_orders
1,Central,HKU
2,Kennedy Town,Discovery Bay
$ ./llm take_order 2
$ ./llm list_orders
1,Central,HKU
$ ./llm take_order 2
Error: order ID 2 is already taken. No changes made.
$ ./llm take_order 3
Error: order ID 3 does not exist.
$ ./llm
Error: no arguments received. Run \"./llm -h\" to see usage.
```

## Testing
This program has been tested using the Python unittesting module.
The `test.sh` script automates the testing and post-testing clean up process.
To run tests, simply run `./test.sh`.