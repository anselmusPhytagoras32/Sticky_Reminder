import customtkinter as ctk
from tkinter import font

ctk.set_appearance_mode("Dark")  
ctk.set_default_color_theme("dark-blue")  

class TaskRow(ctk.CTkFrame):
    def __init__(self, parent, task_text, delete_callback):
        super().__init__(parent, fg_color="transparent")
        self.pack(fill="x", pady=5, padx=10)
        self.delete_callback = delete_callback
        self.is_checked = ctk.BooleanVar(value=False)

        self.checkbox = ctk.CTkCheckBox(
            self, 
            text=task_text, 
            text_color="#ffffff",
            font=("Helvetica", 14),
            variable=self.is_checked,
            command=self.toggle_task,
            corner_radius=20,
            hover_color="#5e455e",
            fg_color="#bba151",      
            border_color="#ffffff",
            checkmark_color="#422e42"
        )
        self.checkbox.pack(side="left", padx=10, pady=10)

        self.del_btn = ctk.CTkButton(
            self, 
            text="×", 
            width=30, 
            height=30,
            fg_color="transparent", 
            text_color="#7d667d",
            hover_color="#563e56",
            font=("Arial", 20, "bold"),
            command=lambda: delete_callback(self)
        )
        self.del_btn.pack(side="right", padx=5)

    def toggle_task(self):
        if self.is_checked.get():
            self.checkbox.configure(text_color="#7d667d") # Dimmed
        else:
            self.checkbox.configure(text_color="#ffffff") # White

