class Order:

    def __init__(self, id, origin, destination, taken):
        self.id = id
        self.origin = origin
        self.destination = destination
        self.taken = taken
    
    def __lt__(self, obj):
        return ((self.id) < (obj.id))
    
    def __gt__(self, obj):
        return ((self.id) > (obj.id))
    
    def __le__(self, obj):
        return ((self.id) <= (obj.id))
    
    def __ge__(self, obj):
        return ((self.id) >= (obj.id))
    
    def __eq__(self, obj):
        return (self.id == obj.id)

    def __str__(self):
        return f"{self.id},{self.origin},{self.destination},{self.taken}"

    def get_id(self):
        return self.id

    def is_taken(self):
        return self.taken
    
    def take(self):
        self.taken = True

    def show(self):
        return(f"{self.id},{self.origin},{self.destination}")
