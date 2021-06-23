from order import Order
import sys

o1 = Order(1, "TST", "SSP", False)
o1.show()
o1.take()
o1.show()

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))