class RecipeView:
    def print_recipe(self, recipe):
        print("=== РЕЦЕПТ ===")
        print("Назва:", recipe.get_name())
        print("Шеф:", recipe.get_chef())
        print("Тип:", recipe.get_type_of_recipe())
        print("Опис:", recipe.get_description())
        print("Відео:", recipe.get_link_to_video())
        print("Інгредієнти:", recipe.get_ingredients())
        print("Кухня:", recipe.get_cuisine())