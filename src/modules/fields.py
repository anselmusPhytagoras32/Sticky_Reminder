import tkinter as tk

class InputField:
    def __init__(self, parent):
        self.parent = parent
        
        self.queue_frame = tk.Frame(parent)
        self.queue_frame.pack(side=tk.TOP, expand=True, fill='both')
        
        self.entry_var = tk.StringVar()
        self.main_entry = tk.Entry(parent, width=40, textvariable=self.entry_var)
        self.main_entry.pack(side=tk.BOTTOM, pady=10)
        
        # For enter key (add feature) 
        self.main_entry.bind('<Return>', lambda event: self.add_queue())

    def add_queue(self):
        task_text = self.entry_var.get()
        
        # Prevent adding empty tasks
        if task_text == "":
            return

        task_label = tk.Label(
            self.queue_frame, 
            text=f"• {task_text}", 
            anchor="w",            
            font=("Arial", 12)
        )
        
        task_label.pack(side=tk.TOP, fill='x', padx=20, pady=2)
        
        self.main_entry.delete(0, tk.END)