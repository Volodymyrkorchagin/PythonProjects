from model import Recipe

class RecipeController:
    def __init__(self):
        self._recipe = None

    def create_recipe(self, name, chef, type_of_recipe, description, link_to_video, ingredients, cuisine):
        self._recipe = Recipe(name, chef, type_of_recipe, description, link_to_video, ingredients, cuisine)

    def get_recipe(self):
        return self._recipe

    def update_name(self, new_name):
        if self._recipe:
            self._recipe.set_name(new_name)

    def update_cuisine(self, new_cuisine):
        if self._recipe:
            self._recipe.set_cuisine(new_cuisine)