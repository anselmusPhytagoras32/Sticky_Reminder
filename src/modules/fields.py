import tkinter as tk

class input_field:
    def __init__(self, parent):
        self.parent = parent
        self.entries = []
        
        self.my_label = tk.Label(parent, text='')
        self.my_label.pack(pady=20)

    def new_entry(self):
        new_list = tk.Entry(self.parent, width=100, textvariable=tk.StringVar())
        new_list.pack(side=tk.TOP,anchor="center")
        self.entries.append(new_list)

    def get_text(self):
        all_text = "".join(input.get() + "\n" for input in self.entries)
        self.my_label.config(text=all_text)