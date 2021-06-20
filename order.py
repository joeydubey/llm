class Order:

    def __init__(self, id, origin, destination, taken):
        self.id = id
        self.origin = origin
        self.destination = destination
        self.taken = taken
    
    def get_id(self):
        return self.id

    def take_order(self):
        self.taken = True

    def show_order(self):
        print(str(self.id) + "," + self.origin + "," + self.destination + str(self.taken))
