from ShoeController import ShoeController
from Shoe.ShoeView import ShoeView

def main():
    controller = ShoeController()
    view = ShoeView()

    controller.create_shoe(
        "чоловіче",
        "кросівки",
        "чорний",
        2500,
        "Nike",
        42
    )

    shoe = controller.get_shoe()
    view.print_shoe(shoe)

    controller.update_price(2200)
    controller.update_color("білий")

    print("\nПісля оновлення:")
    view.print_shoe(controller.get_shoe())

if __name__ == "__main__":
    main()