import tkinter as tk

class input_field:
    def __init__(self, parent):
        self.parent = parent
        self.entries = []

    def new_list(self):
        new_list = tk.Entry(self.parent, width=100, textvariable=tk.StringVar())
        new_list.pack(side=tk.TOP,anchor="center")
        self.entries.append(new_list)