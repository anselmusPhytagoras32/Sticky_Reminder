import customtkinter as ctk
from modules.TaskList import TaskRow
class Actions:
    def __init__(self, app_instance):
        self.app = app_instance

        self.scroll_frame = ctk.CTkScrollableFrame(
            self.app, 
            fg_color="transparent", 
            scrollbar_button_color=self.app.colors["bg_header"],
            scrollbar_button_hover_color=self.app.colors["accent"]
        )
        self.scroll_frame.pack(fill="both", expand=True, padx=0, pady=10)

        self.add_btn = ctk.CTkButton(
            self.app,
            text="+",
            font=("Arial", 30),
            width=60,
            height=60,
            corner_radius=30,
            fg_color="#ffffff",
            text_color=self.app.colors["bg_body"],
            hover_color="#e0e0e0",
            command=self.open_input_dialog
        )
        self.add_btn.place(relx=0.5, rely=0.9, anchor="center")

    def add_task(self, text):
        new_row = TaskRow(self.scroll_frame, text, self.delete_task)
        self.app.tasks.append(new_row)
        self.update_task_count()

    def delete_task(self, task_widget):
        if task_widget in self.app.tasks:
            self.app.tasks.remove(task_widget)
            task_widget.destroy()
            self.update_task_count()

    def update_task_count(self):
        count = len(self.app.tasks)
        self.app.count_lbl.configure(text=f"{count} tasks")

    def open_input_dialog(self):
        dialog = ctk.CTkInputDialog(text="Enter new task:", title="New Task")
        if new_task_text := dialog.get_input():
            self.add_task(new_task_text)

           