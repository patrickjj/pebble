from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

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
    title = new_recipe.get('title')
    ingredients = new_recipe.get('ingredients')
    instructions = new_recipe.get('instructions')
    cursor.execute('INSERT INTO recipes (title, ingredients, instructions) VALUES (?, ?, ?)',
                   (title, ingredients, instructions))
    conn.commit()

    return jsonify({'message': 'Recipe added successfully'})

# Define endpoint to get a specific recipe by ID
@app.route('/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    cursor.execute('SELECT * FROM recipes WHERE id = ?', (recipe_id,))
    recipe = cursor.fetchone()
    if recipe:
        return jsonify({'recipe': recipe})
    return jsonify({'message': 'Recipe not found'}), 404

@app.route('/recipes/<int:recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    update_recipe = request.get_json()  # Get JSON data from the request body
    title = update_recipe.get('title')
    ingredients = update_recipe.get('ingredients')
    instructions = update_recipe.get('instructions')
    cursor.execute('''UPDATE recipes
                SET title = ?, ingredients= ?, instructions= ?
                WHERE id = ?;''', (title, ingredients, instructions, recipe_id))
    conn.commit()

    return jsonify({'message': 'Recipe updated successfully'})

@app.route('/recipes', methods=['GET'])
def get_all_recipes():
    cursor.execute('SELECT * FROM recipes')
    recipes = cursor.fetchall()
    row_headers=[x[0] for x in cursor.description]
    json_data = []
    for result in recipes:
            json_data.append(dict(zip(row_headers,result)))
    if recipes:
        return jsonify({'recipes': json_data})
    return jsonify({'message': 'Recipe not found'}), 404

@app.route('/recipes/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):

    # Execute the DELETE query
    cursor.execute("DELETE FROM recipes WHERE id = ?", (recipe_id,))
    conn.commit()

    if cursor.rowcount > 0:
        return jsonify({'message': 'Recipe deleted successfully'}), 200
    else:
        return jsonify({'message': 'Recipe not found'}), 404
    
@app.route('/recipes/add-category', methods=['POST'])
def update_category():

    # Execute the DELETE query
    cursor.execute('''ALTER TABLE recipes
                    ADD rating TINYINT;''')
    conn.commit()

    if cursor.rowcount > 0:
        return jsonify({'message': 'Recipe deleted successfully'}), 200
    else:
        return jsonify({'message': 'Recipe not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
