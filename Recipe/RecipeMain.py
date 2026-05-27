from RecipeController import RecipeController
from RecipeView import RecipeView

def main():
    controller = RecipeController()
    view = RecipeView()

    controller.create_recipe(
        "піцца",
        "Бон",
        "швидка їжа",
        "Смачна піцца",
        "https://goo.su/niBz9",
        ["томат", "м'ясо", "тісто"],
        "Italian"
    )

    recipe = controller.get_recipe()
    view.print_recipe(recipe)

    controller.update_name("Піца Маргарита")
    controller.update_cuisine("Italian")

    print("\nПісля оновлення:")
    view.print_recipe(controller.get_recipe())

if __name__ == "__main__":
    main()