import tkinter as tk

def history_button(parent):
    def open_new_window():
        new_win = tk.Toplevel(parent)
        new_win.title("New List")
        tk.Label(new_win, text="This is your new list window").pack(padx=20, pady=20)

    button_history = tk.Button(parent, text="Edit List", fg="black", command=open_new_window)
    button_history.pack(side=tk.RIGHT, anchor="s")

def add_button(parent):
    def add_list():
        new_list = tk.Entry(parent, width=7, textvariable=tk.StringVar())
        new_list.pack(side=tk.TOP,anchor="center")
    
    button_add = tk.Button(parent, text="Add Task", fg="black", command=add_list)
    button_add.pack(side=tk.BOTTOM, anchor="s")

def delete_button(parent):
    # Pass the actual frame instance (parent) instead of the class tk.Frame
    button_quit = tk.Button(parent, text="QUIT", fg="black", command=parent.winfo_toplevel().destroy)
    button_quit.pack(side=tk.LEFT, anchor="s")