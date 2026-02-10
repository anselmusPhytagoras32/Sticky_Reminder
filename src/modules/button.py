import tkinter as tk

from modules.fields import input_field

def edit_button(parent):
    button_edit = tk.Button(parent, width=50, text="Edit List", fg="black")
    button_edit.pack(side=tk.BOTTOM, anchor="s")

def add_button(parent, manager_instance):
    button_add = tk.Button(parent, width=50, text="Add Task", fg="black", command=manager_instance.get_text)
    button_add.pack(side=tk.BOTTOM, anchor="s")

def delete_button(parent):
    # Pass the actual frame instance (parent) instead of the class tk.Frame
    button_quit = tk.Button(parent, width=50, text="Delete", fg="black")
    button_quit.pack(side=tk.BOTTOM, anchor="s")