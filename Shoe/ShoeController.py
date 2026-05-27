from Shoe.ShoeModel import Shoe

class ShoeController:
    def __init__(self):
        self._shoe = None

    def create_shoe(self, shoe_type, kind, color, price, manufacturer, size):
        self._shoe = Shoe(shoe_type, kind, color, price, manufacturer, size)

    def get_shoe(self):
        return self._shoe

    def update_price(self, new_price):
        if self._shoe:
            self._shoe.set_price(new_price)

    def update_color(self, new_color):
        if self._shoe:
            self._shoe.set_color(new_color)