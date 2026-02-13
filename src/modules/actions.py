import json
import os
import sys
import customtkinter as ctk

from modules.TaskList import TaskRow

class Actions:
    def __init__(self, app_instance):
        self.app = app_instance

        # Check if the app is running as a script or an executable to find the right path
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        else:
            application_path = os.path.dirname(os.path.abspath(__file__))

        # Set the destination folder for the saved files
        self.folder_path = os.path.join(application_path, "files")

        # Create the folder if it is missing
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)

        self.file_path = os.path.join(self.folder_path, "data.json")

        self.scroll_frame = ctk.CTkScrollableFrame(
            self.app, 
            fg_color="transparent", 
            scrollbar_button_color=self.app.colors["bg_header"],
            scrollbar_button_hover_color=self.app.colors["accent"]
        )
        self.scroll_frame.pack(fill="both", expand=True, padx=0, pady=(10, 80))

        self.bottom_frame = ctk.CTkFrame(self.app, fg_color="transparent")
        self.bottom_frame.place(relx=0.5, rely=0.9, anchor="center", relwidth=0.85)

        self.add_btn = ctk.CTkButton(
            self.bottom_frame,
            text="+",
            font=("Arial", 30),
            width=60,
            height=60,
            corner_radius=30,
            fg_color="#ffffff",
            text_color=self.app.colors["bg_body"],
            hover_color="#e0e0e0",
            command=self.toggle_input_field
        )
        self.add_btn.pack(side="right", padx=(10, 0))

        self.task_entry = ctk.CTkEntry(
            self.bottom_frame,
            placeholder_text="What needs to be done?",
            height=50,
            corner_radius=25,
            border_width=0,
            fg_color="#ffffff",
            text_color="black",
            font=("Arial", 16)
        )
        self.task_entry.bind("<Return>", self.save_new_task_event)
        
        # Restore saved tasks when the app launches
        self.load_tasks()

    def toggle_input_field(self):
        if not self.task_entry.winfo_ismapped():
            self.task_entry.pack(side="right", fill="x", expand=True)
            self.task_entry.focus()
            self.add_btn.configure(text="✓", fg_color=self.app.colors["accent"])
        else:
            self.save_new_task_event()

    def save_new_task_event(self, event=None):
        text = self.task_entry.get()
        if text.strip():
            self.add_task(text) 
            self.task_entry.delete(0, "end")
        self.task_entry.pack_forget()
        self.add_btn.configure(text="+", fg_color="#ffffff") 

    def add_task(self, text, is_done=False, save=True):
        new_row = TaskRow(self.scroll_frame, text, self.delete_task, self.save_tasks, is_done)
        self.app.tasks.append(new_row)
        self.update_task_count()
        
        if save:
            self.save_tasks()

    def delete_task(self, task_widget):
        if task_widget in self.app.tasks:
            self.app.tasks.remove(task_widget)
            task_widget.destroy()
            self.update_task_count()
            self.save_tasks()

    def update_task_count(self):
        count = len(self.app.tasks)
        self.app.count_lbl.configure(text=f"{count} tasks")

    # Save the current list of tasks to the JSON file
    def save_tasks(self):
        data = []
        data.extend(
            {"text": row.checkbox.cget("text"), "done": row.is_checked.get()}
            for row in self.app.tasks
        )
        try:
            with open(self.file_path, "w") as f:
                json.dump(data, f)
        except Exception as e:
            print(f"Error saving: {e}")

    # Read the JSON file and repopulate the list
    def load_tasks(self):
        # Check if the file exists before reading
        if not os.path.exists(self.file_path):
            return 
        
        try:
            with open(self.file_path, "r") as f:
                data = json.load(f)
                for item in data:
                    self.add_task(item["text"], is_done=item["done"], save=False)
        except Exception as e:
            print(f"Error loading: {e}")