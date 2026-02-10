import tkinter as tk

from modules.fields import input_field

def history_button(parent):
    def open_new_window():
        new_win = tk.Toplevel(parent)
        new_win.title("New List")
        tk.Label(new_win, text="This is your new list window").pack(padx=20, pady=20)

    button_history = tk.Button(parent, width=10, text="Edit List", fg="black", command=open_new_window)
    button_history.pack(side=tk.RIGHT, anchor="s")

def add_button(parent, manager_instance):
    button_add = tk.Button(parent, width=10, text="Add Task", fg="black", command=manager_instance.new_list)
    button_add.pack(side=tk.LEFT, anchor="s")

def delete_button(parent):
    def open_new_window():
        new_win = tk.Toplevel(parent)
        new_win.title("New List")
        tk.Label(new_win, text="Select List to Delete").pack(padx=20, pady=20)

    # Pass the actual frame instance (parent) instead of the class tk.Frame
    button_quit = tk.Button(parent, width=10, text="Delete", fg="black", command=open_new_window)
    button_quit.pack(side=tk.LEFT, anchor="s")