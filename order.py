class Order:
    """
    A class used to represent an Order

    Attributes
    ----------
    id: int
        the unique order id that identifies each order
    
    origin: str
        where the order is to be shipped from

    destination: str
        where the order is to be shipped to

    taken: bool
        stores whether the order has been taken or not
    
    Methods
    -------
    show() -> str
        returns a formatted string representation of the order
    """
    id: int
    origin: str
    destination: str
    taken: bool

    def __init__(self, id, origin, destination, taken=False) -> None:
        """
        Constructor for Order class

        Parameters
        ----------
        id: int
            the unique order id that identifies each order
        
        origin: str
            where the order is to be shipped from

        destination: str
            where the order is to be shipped to

        taken: bool, optional
            stores whether the order has been taken or not (default is False)
        
        """
        self.id = id
        self.origin = origin
        self.destination = destination
        self.taken = taken
    
    def __lt__(self, obj) -> bool:
        """
        Determines if the order is less than (<) another given order.
        The order is less than another order if its "id" attribute is smaller
        than the other order's "id" attribute.

        Parameters
        ----------
        obj: Order
            the other order that the current order is to be compared to.
        
        """
        return ((self.id) < (obj.id))
    
    def __gt__(self, obj) -> bool:
        """
        Determines if the order is greater than (>) another given order.
        The order is greater than another order if its "id" attribute is larger
        than the other order's "id" attribute.

        Parameters
        ----------
        obj: Order
            the other order that the current order is to be compared to.
        
        """
        return ((self.id) > (obj.id))
    
    def __le__(self, obj) -> bool:
        """
        Determines if the order is less than or equal to (<=) another given order.
        The order is less than or equal to another order if its "id" attribute
        is smaller than or equal to the other order's "id" attribute.

        Parameters
        ----------
        obj: Order
            the other order that the current order is to be compared to.
        
        """
        return ((self.id) <= (obj.id))
    
    def __ge__(self, obj) -> bool:
        """
        Determines if the order is greater than or equal to (>=)
        another given order.
        The order is greater than or equal to another order if its "id" attribute
        is larger than or equal to the other order's "id" attribute.

        Parameters
        ----------
        obj: Order
            the other order that the current order is to be compared to.
        
        """
        return ((self.id) >= (obj.id))
    
    def __eq__(self, obj) -> bool:
        """
        Determines if the order is equal to (=) another given order.
        The order is equal to another order if its "id" attribute is equal to
        the other order's "id" attribute.

        Parameters
        ----------
        obj: Order
            the other order that the current order is to be compared to.
        
        """
        return (self.id == obj.id)

    def __str__(self) -> str:
        """
        Returns a formatted string representation of the order displaying
        all of its attributes.
        
        """
        return f"{self.id},{self.origin},{self.destination},{self.taken}"

    def show(self) -> str:
        """
        Returns a formatted string representation of the order displaying
        only the required attributes "id", "origin" and "destination".
        
        """
        return(f"{self.id},{self.origin},{self.destination}")
