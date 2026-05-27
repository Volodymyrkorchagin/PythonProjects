class Flat:
    def __init__(self, square, price):
        self.square = square
        self.price = price

    def __eq__(self, other):
        return self.square == other.square

    def __ne__(self, other):
        return self.square != other.square

    def __lt__(self, other):
        return self.price < other.price

    def __le__(self, other):
        return self.price <= other.price

    def __gt__(self, other):
        return self.price > other.price

    def __ge__(self, other):
        return self.price >= other.price
