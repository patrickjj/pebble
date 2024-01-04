import sqlite3
# Connect to SQLite database
# conn = sqlite3.connect('recipes.db', check_same_thread=False)
# cursor = conn.cursor()
# cursor.execute("UPDATE recipes SET rating = ?, title = ?, ingredients = ?, instructions = ?, link = ?, region = ? WHERE id = ?", (new_rating, title, ingredients, instructions, link, region, recipe_id))


try:
    conn = sqlite3.connect('exoplanets.db', check_same_thread=False)
    cursor = conn.cursor()
    # Open and read the SQL file
    sql_file = open('planets_data.sql', 'r')
    sql_text = sql_file.read()
    sql_file.close()
    # Execute the SQL commands
    cursor = conn.cursor()
    cursor.executescript(sql_text)

    # Close the connection
    conn.close()
except sqlite3.Error as e:
    print("SQLite error:", e)