class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __sub__(self, other):
        new_radius = self.radius - other.radius
        if new_radius < 0:
            raise ValueError("Radius cannot be negative")
        return Circle(new_radius)

    def __iadd__(self, other):
        self.radius += other.radius
        return self

    def __isub__(self, other):
        new_radius = self.radius - other.radius
        if new_radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = new_radius
        return self