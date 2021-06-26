class Order:
    id: int
    origin: str
    destination: str
    taken: bool

    def __init__(self, id, origin, destination, taken) -> None:
        self.id = id
        self.origin = origin
        self.destination = destination
        self.taken = taken
    
    def __lt__(self, obj) -> bool:
        return ((self.id) < (obj.id))
    
    def __gt__(self, obj) -> bool:
        return ((self.id) > (obj.id))
    
    def __le__(self, obj) -> bool:
        return ((self.id) <= (obj.id))
    
    def __ge__(self, obj) -> bool:
        return ((self.id) >= (obj.id))
    
    def __eq__(self, obj) -> bool:
        return (self.id == obj.id)

    def __str__(self) -> str:
        return f"{self.id},{self.origin},{self.destination},{self.taken}"

    def get_id(self) -> int:
        return self.id

    def is_taken(self) -> bool:
        return self.taken
    
    def take(self) -> None:
        self.taken = True

    def show(self) -> str:
        return(f"{self.id},{self.origin},{self.destination}")
