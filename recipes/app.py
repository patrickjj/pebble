from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3
import recipes as r
import pandas as pd

app = Flask(__name__)
CORS(app)
# Connect to SQLite database
conn = sqlite3.connect('recipes.db', check_same_thread=False)
cursor = conn.cursor()


# Close the cursor and connection after the application ends
# @app.teardown_appcontext
# def close_connection(exception):
#     cursor.close()
#     conn.close()

# Define endpoint to get all recipes
@app.route('/recipes', methods=['POST'])
def add_recipe():
    new_recipe = request.get_json()  # Get JSON data from the request body
    new_rating = new_recipe.get('rating')
    title = new_recipe.get('title')
    ingredients = new_recipe.get('ingredients')
    instructions = new_recipe.get('instructions')
    link = new_recipe.get('link')
    region = new_recipe.get('region')
    cursor.execute('INSERT INTO recipes (rating, title, ingredients, instructions, link, region) VALUES (?, ?, ?, ?, ?, ?)',
                   (new_rating, title, ingredients, instructions, link, region))
    conn.commit()

    return jsonify({'message': 'Recipe added successfully'})

# Define endpoint to get a specific recipe by ID
@app.route('/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    cursor.execute('SELECT * FROM recipes WHERE id = ?', (recipe_id,))
    recipe = cursor.fetchone()
    row_headers=[x[0] for x in cursor.description]
    json_data = []
    json_data.append(dict(zip(row_headers,recipe)))
    if json_data:
        return jsonify({'recipes': json_data})
    return jsonify({'message': 'Recipe not found'}), 404


@app.route('/recipes', methods=['GET'])
def get_all_recipes():
    cursor.execute('SELECT * FROM recipes')
    recipes = cursor.fetchall()
    row_headers=[x[0] for x in cursor.description]
    json_data = []
    for result in recipes:
            json_data.append(dict(zip(row_headers,result)))
    if recipes:
        # df = pd.json_normalize(json_data)
        # print(df)
        # recipe_list = [r.Recipe(**row) for row in df.to_dict('records')]
        # print(recipe_list)
        return jsonify({'recipes': json_data})
    
    
    return jsonify({'message': 'Recipe not found'}), 404

@app.route('/recipes/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):

    cursor.execute("DELETE FROM recipes WHERE id = ?", (recipe_id,))
    conn.commit()

    if cursor.rowcount > 0:
        return jsonify({'message': 'Recipe deleted successfully'}), 200
    else:
        return jsonify({'message': 'Recipe not found'}), 404
    
@app.route('/recipes/<int:recipe_id>/update', methods=['POST'])
def update_recipe(recipe_id):

    update_recipe = request.get_json()
    print(update_recipe)
    new_rating = update_recipe.get('rating')
    title = update_recipe.get('title')
    ingredients = update_recipe.get('ingredients')
    instructions = update_recipe.get('instructions')
    link = update_recipe.get('link')
    region = update_recipe.get('region')

    cursor.execute("UPDATE recipes SET rating = ?, title = ?, ingredients = ?, instructions = ?, link = ?, region = ? WHERE id = ?", (new_rating, title, ingredients, instructions, link, region, recipe_id))

    conn.commit()

    return jsonify({'message': 'Recipe updated successfully'})


if __name__ == '__main__':
    app.run(debug=True)
