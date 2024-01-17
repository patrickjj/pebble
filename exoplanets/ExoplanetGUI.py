import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ExoplanetAPI import ExoplanetAPI
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class ExoplanetGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Exoplanet Explorer")
        self.exoplanet_api = ExoplanetAPI()
        self.mode_var = tk.StringVar(value="Planets")

        self.create_widgets()

    def create_widgets(self):
        self.min_value_entry = ttk.Entry(self.root, width=10)
        self.max_value_entry = ttk.Entry(self.root, width=10)

        mode_dropdown = ttk.Combobox(self.root, textvariable=self.mode_var, values=["Planets", "Systems"], state="readonly")
        mode_dropdown.bind("<<ComboboxSelected>>", self.update_labels)

        update_button = ttk.Button(self.root, text="Update Graphs", command=self.update_graphs)

        instructions_label = ttk.Label(self.root, text="Select mode and enter min and max values:")

        instructions_label.grid(row=0, column=0, columnspan=3, pady=0)
        ttk.Label(self.root, text="Mode:").grid(row=1, column=0)
        mode_dropdown.grid(row=1, column=1, pady=5)
        ttk.Label(self.root, text="").grid(row=2, column=0)
        self.min_value_entry.grid(row=2, column=1, pady=5)
        ttk.Label(self.root, text="").grid(row=3, column=0)
        self.max_value_entry.grid(row=3, column=1, pady=5)
        update_button.grid(row=4, column=0, columnspan=2, pady=10)

    def update_labels(self, event):
        for widget in self.root.winfo_children():
            if isinstance(widget, ttk.Label):
                widget.config(text="")

        mode = self.mode_var.get()
        if mode == "Planets":
            ttk.Label(self.root, text="Min Mass:").grid(row=2, column=0, sticky="e")
            ttk.Label(self.root, text="Max Mass:").grid(row=3, column=0, sticky="e")
        elif mode == "Systems":
            ttk.Label(self.root, text="Min Num Stars:").grid(row=2, column=0, sticky="e")
            ttk.Label(self.root, text="Max Num Stars:").grid(row=3, column=0, sticky="e")

    def update_graphs(self):
        try:
            mode = self.mode_var.get()
            min_value = float(self.min_value_entry.get())
            max_value = float(self.max_value_entry.get())

            if min_value < 0 or max_value < 0 or min_value > max_value:
                messagebox.showerror("Error", "Invalid input. Please check your values.")
                return

           
            
            df = self.exoplanet_api.query_min_max_planets(min_value, max_value)
            plt.figure(figsize=(8, 6))
            planet_masses = df['planet_mass_ratio'] 
            planet_radii = df['planet_radius']  
            plt.scatter(planet_masses, planet_radii,  s=planet_radii ** 2 * 200/df.size)
            plt.xlabel("Planet Mass (Earth Mass Ratio)", fontsize=12)
            plt.ylabel("Planet Radius (Earth Radius Ratio)", fontsize=12)
            plt.title("Planet Mass vs. Radius", fontsize=14)
            plt.grid(True)

            for i, row in df.iterrows():
                plt.annotate(row['planet_name'], (planet_masses[i], planet_radii[i]))

            plt.show()



        except FileNotFoundError:
            messagebox.showerror("Error", "Invalid input. Please enter numerical values.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExoplanetGUI(root)
    app.update_labels(None)
    root.mainloop()
