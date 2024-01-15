class Recipe:
    def __init__(self, ingredients, country_of_origin, rating, directions, link):
        self.ingredients = ingredients
        self.country_of_origin = country_of_origin
        self.rating = rating
        self.directions = directions
        self.link = link

    def __repr__(self):
        return f"Recipe({self.ingredients}, {self.country_of_origin}, {self.rating}, {self.directions}, {self.link})"