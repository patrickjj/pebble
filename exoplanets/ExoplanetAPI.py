import sqlite3
import pandas as pd


class ExoplanetAPI:
    def __init__(self, db_path='exoplanets.db'):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path, check_same_thread=False)

    def query_min_max_planets(self, min_value, max_value):
        sql_query = f"""
            SELECT
            planet.pl_name AS planet_name,
            system.hostname AS system_name,
            system.sy_pnum AS number_of_planets,
            planet.pl_masse AS planet_mass_ratio,
            planet.pl_rade
            FROM planet
            JOIN system ON planet.hostname = system.hostname
            WHERE planet.pl_masse BETWEEN {min_value} AND {max_value};
        """
        result = self.conn.execute(sql_query).fetchall()
        df = pd.DataFrame(result, columns=['planet_name', 'system_name', 'number_of_planets', 'planet_mass_ratio', 'planet_radius'])

        return df
    
    
    def query_systems(self, min_stars, max_stars):
        sql_query = f"""
            SELECT 
                system.hostname AS system_name,
                system.sy_snum AS number_of_stars,
                planet.pl_name AS planet_name
            FROM system
            JOIN planet ON system.hostname = planet.hostname
            WHERE system.sy_snum BETWEEN {min_stars} AND {max_stars};
        """
        result = self.conn.execute(sql_query).fetchall()
        df = pd.DataFrame(result, columns=['system_name', 'number_of_stars', 'planet_name'])
        return df