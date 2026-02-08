import tkinter as tk

def history_button(parent):
    def open_new_window():
        new_win = tk.Toplevel(parent)
        new_win.title("New List")
        tk.Label(new_win, text="This is your new list window").pack(padx=20, pady=20)

    button_history = tk.Button(parent, text="Add New List", fg="black", command=open_new_window)
    button_history.pack(side=tk.LEFT, padx=5)

def add_button(parent):
    def add_list():
        new_list = tk.Entry(parent, width=7, textvariable=tk.StringVar())
        new_list.pack(side=tk.RIGHT, padx=5)
    
    button_add = tk.Button(parent, text="Add Task", fg="black", command=add_list)
    button_add.pack(side=tk.RIGHT, padx=5 )

def delete_button(parent):
    # Pass the actual frame instance (parent) instead of the class tk.Frame
    button_quit = tk.Button(parent, text="QUIT", fg="black", command=parent.winfo_toplevel().destroy)
    button_quit.pack(side=tk.LEFT, padx=5)