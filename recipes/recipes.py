import pandas as pd

class Recipe:
    def __init__(self, ingredients, region, rating, instructions, link, title, id, notes):
        self.ingredients = ingredients
        self.region = region
        self.rating = rating
        self.instructions = instructions
        self.link = link
        self.title = title
        self.id = id
        self.notes = notes

    def __repr__(self):
        return f"Recipe({self.ingredients}, {self.region}, {self.rating}, {self.instructions}, {self.link}, {self.title})"

def recipes_to_df(recipes):
    df_columns = ["Ingredients", "Country of Origin", "Rating", "instructions", "Link", "title"]
    df_data = []

    for recipe in recipes:
        row = [
            ", ".join(recipe.ingredients),
            recipe.region,
            recipe.rating,
            recipe.instructions,
            recipe.link,
            recipe.title
        ]
        df_data.append(row)

    return pd.DataFrame(df_data, columns=df_columns)

def filter_by_ingredients(df, ingredients):
    filtered_df = df[df["Ingredients"].apply(lambda x: all(ingredient in x for ingredient in ingredients))]
    return filtered_df

my_recipes = [
    Recipe(
        ingredients=["chicken", "onion", "garlic", "curry powder"],
        region="India",
        rating=4.5,
        instructions="Cook the chicken in a pan with some oil, then add the onion and garlic...",
        link="test",
        title="Chicken Curry",
        id=2,
        notes="notes"
    ),
    Recipe(
        ingredients=["beef", "mushrooms", "onion", " Worcestershire sauce"],
        region="USA",
        rating=4.2,
        instructions="Brown the beef in a pan, then add the onion and mushrooms...",
        link="test",
        title="Beef Stroganoff",
        id=3,
        notes="notes"

    )
]

df = recipes_to_df(my_recipes)
print(filter_by_ingredients(df, ["beef", "onion"]))
# print(df)