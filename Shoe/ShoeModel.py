class Shoe:
    def __init__(self, shoe_type, kind, color, price, manufacturer, size):
        self._shoe_type = shoe_type
        self._kind = kind
        self._color = color
        self._price = price
        self._manufacturer = manufacturer
        self._size = size

    def get_type(self):
        return self._shoe_type

    def get_kind(self):
        return self._kind

    def get_color(self):
        return self._color

    def get_price(self):
        return self._price

    def get_manufacturer(self):
        return self._manufacturer

    def get_size(self):
        return self._size

    def set_price(self, price):
        self._price = price

    def set_color(self, color):
        self._color = color
