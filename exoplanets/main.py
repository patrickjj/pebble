import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# try:
#     conn = sqlite3.connect('exoplanets.db', check_same_thread=False)
#     cursor = conn.cursor()
#     sql_file = open('planets_data.sql', 'r')
#     sql_text = sql_file.read()
#     sql_file.close()
#     cursor = conn.cursor()
#     cursor.executescript(sql_text)
#     conn.close()
# except sqlite3.Error as e:
#     print("SQLite error:", e)


conn = sqlite3.connect('exoplanets.db', check_same_thread=False)
cursor = conn.cursor()
# Planets with 2 stars like tatooine with earth mass and radius ratios
cursor.execute('''SELECT s.hostname, s.sy_snum, p.pl_name, p.pl_rade, p.pl_masse, p.pl_orbsmax FROM system as s, planet as p WHERE s.sy_snum == 2 AND s.hostname = p.hostname AND
               p.pl_rade IS NOT NULL AND p.pl_masse IS NOT NULL AND p.pl_orbsmax IS NOT NULL''')
systems = cursor.fetchall()
df = pd.DataFrame(systems) 
print(df)
plt.figure(figsize=(20,20))
plt.subplot(2,1,2)
plt.scatter(df[3], df[4], s=20, c=df[5], marker='8', cmap='gist_heat')
plt.colorbar(label='Semi Major Axis (AU)', extend='both')
plt.xticks(fontsize=20)
plt.yticks(fontsize=12)
plt.xlabel("Radius (Ratio to Earth Radius)", fontsize = 30)
plt.ylabel("Mass (Ratio to Earth Mass)", fontsize = 30)
plt.show()