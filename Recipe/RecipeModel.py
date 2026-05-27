class Recipe:
    def __init__(self, name, chef, type_of_recipe, description, link_to_video, ingredients, cuisine):
        self._name = name
        self._chef = chef
        self._type_of_recipe = type_of_recipe
        self._description = description
        self._link_to_video = link_to_video
        self._ingredients = ingredients
        self._cuisine = cuisine

    def get_name(self):
        return self._name

    def get_chef(self):
        return self._chef

    def get_type_of_recipe(self):
        return self._type_of_recipe

    def get_description(self):
        return self._description

    def get_link_to_video(self):
        return self._link_to_video

    def get_ingredients(self):
        return self._ingredients

    def get_cuisine(self):
        return self._cuisine

    def set_name(self, name):
        self._name = name

    def set_cuisine(self, cuisine):
        self._cuisine = cuisine