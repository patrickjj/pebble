import tkinter as tk

window = tk.Tk()
window.title("To-Do List")
window.configure(background="#f2f2f2")  

label = tk.Label(window, text="To-Do List:", background="#f2f2f2", foreground="#333333")
label.pack()
listbox = tk.Listbox(window, height=10, width=40, background="#f2f2f2", foreground="#333333", selectmode=tk.MULTIPLE)
listbox.pack()


checkbox = tk.Checkbutton(window, text="Select items to remove", variable=tk.BooleanVar(value=False))
checkbox.pack()

entry_box = tk.Entry(window, background="#f2f2f2", foreground="#333333")
entry_box.pack()

def add_item():
    item = entry_box.get()
    listbox.insert(tk.END, item)
    entry_box.delete(0, tk.END)



def remove_checked_items():
    selected_items = []
    for item in listbox.curselection():
        selected_items.append(listbox.get(item))
    for item in selected_items:
        listbox.delete(tk.CURRENT)



add_button = tk.Button(window, text="Add new item", command=add_item)

remove_button = tk.Button(window, text="Remove checked items", command=remove_checked_items)

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
add_button.grid(column=0, row=1)
remove_button.grid(column=1, row=1)


window.mainloop()