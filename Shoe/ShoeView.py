class ShoeView:
    def print_shoe(self, shoe):
        print("=== Інформація про взуття ===")
        print("Тип:", shoe.get_type())
        print("Вид:", shoe.get_kind())
        print("Колір:", shoe.get_color())
        print("Ціна:", shoe.get_price())
        print("Виробник:", shoe.get_manufacturer())
        print("Розмір:", shoe.get_size())