import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt





conn = sqlite3.connect('exoplanets.db', check_same_thread=False)
cursor = conn.cursor()
# Planets with 2 stars like tatooine with earth mass and radius ratios
cursor.execute('''SELECT s.hostname, s.sy_snum, p.pl_name, p.pl_rade, p.pl_masse, p.pl_orbsmax FROM system as s, planet as p WHERE s.sy_snum == 2 AND s.hostname = p.hostname AND
               p.pl_rade IS NOT NULL AND p.pl_masse IS NOT NULL AND p.pl_orbsmax IS NOT NULL''')
systems = cursor.fetchall()
df = pd.DataFrame(systems, columns=['host_name', 'num_stars', 'number_of_planets', 'planet_mass_ratio', 'planet_radius', 'semi_orbital_max'])


plt.figure(figsize=(20,20))
plt.subplot(2,1,2)
plt.scatter(df['planet_mass_ratio'], df['planet_radius'], s=20, c=df['semi_orbital_max'], marker='8', cmap='gist_heat')
plt.colorbar(label='Semi Major Axis (AU)', extend='both')
plt.xticks(fontsize=20)
plt.yticks(fontsize=12)
plt.xlabel("Radius (Ratio to Earth Radius)", fontsize = 30)
plt.ylabel("Mass (Ratio to Earth Mass)", fontsize = 30)
plt.show()



sql = """
SELECT
  planet.pl_name AS planet_name,
  system.hostname AS system_name,
  system.sy_pnum AS number_of_planets,
  planet.pl_masse AS planet_mass_ratio,
  planet.pl_rade
FROM planet
JOIN system ON planet.hostname = system.hostname
WHERE planet.pl_masse BETWEEN 0.5 AND 1.5;
"""

result = conn.execute(sql).fetchall()

df = pd.DataFrame(result, columns=['planet_name', 'system_name', 'number_of_planets', 'planet_mass_ratio', 'planet_radius'])

plt.figure(figsize=(8, 6))


planet_masses = df['planet_mass_ratio'] 
planet_radii = df['planet_radius']  


plt.scatter(planet_masses, planet_radii,  s=planet_radii ** 2 * 200)


plt.xlabel("Planet Mass (Earth Mass Ratio)", fontsize=12)
plt.ylabel("Planet Radius (Earth Radius Ratio)", fontsize=12)
plt.title("Planet Mass vs. Radius", fontsize=14)
plt.grid(True)

for i, row in df.iterrows():
    plt.annotate(row['planet_name'], (planet_masses[i], planet_radii[i]))

plt.show()
