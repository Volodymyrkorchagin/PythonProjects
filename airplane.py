class Airplane:
    def __init__(self, passenger, capacity, model):
        self.passenger = passenger
        self.capacity = capacity
        self.model = model

    def __eq__(self, other):
        return self.capacity == other.capacity and self.model == other.model

    def __lt__(self, other):
        return self.capacity < other.capacity

    def __le__(self, other):
        return self.capacity <= other.capacity

    def __gt__(self, other):
        return self.capacity > other.capacity

    def __ge__(self, other):
        return self.capacity >= other.capacity

    def __add__(self, other):
        new_passenger = self.passenger + other.passenger
        if new_passenger > self.capacity:
            new_passenger = self.capacity
        return Airplane(new_passenger, self.capacity, self.model)

    def __sub__(self, other):
        new_passenger = self.passenger - other.passenger
        if new_passenger < 0:
            raise ValueError("Passenger cannot be negative")
        return Airplane(new_passenger, self.capacity, self.model)

    def __iadd__(self, other):
        self.passenger += other.passenger
        return self

    def __isub__(self, other):
        new_passenger = self.passenger - other.passenger
        if new_passenger < 0:
            raise ValueError("Passenger cannot be negative")
        self.passenger = new_passenger
        return self