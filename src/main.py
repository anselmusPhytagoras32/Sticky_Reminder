import customtkinter as ctk

from modules.actions import Actions

ctk.set_appearance_mode("Dark")  
ctk.set_default_color_theme("dark-blue")  

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window Setup
        self.title("To do")
        self.geometry("380x650")
        self.resizable(False, False)

        self.colors = {
            "bg_body": "#422e42",
            "bg_header": "#563e56", 
            "accent": "#bba151"
        }

        self.configure(fg_color=self.colors["bg_body"])

        self.header = ctk.CTkFrame(self, fg_color=self.colors["bg_header"], height=100, corner_radius=0)
        self.header.pack(fill="x", side="top")

        # Header Grid Layout
        self.header.columnconfigure(0, weight=1)
        self.header.columnconfigure(2, weight=2) # Date and Count
        self.header.columnconfigure(4, weight=1)

        self.date_lbl = ctk.CTkLabel(self.header, text="30 FEBRUARY, MON", font=("Helvetica", 14, "bold"), text_color="white")
        self.date_lbl.grid(row=0, column=2, sticky="s")
        
        self.count_lbl = ctk.CTkLabel(self.header, text="0 tasks", font=("Helvetica", 12), text_color=self.colors["accent"])
        self.count_lbl.grid(row=1, column=2, sticky="n")

        self.actions = Actions(self)
        self.tasks = []

        self.actions.add_task("Create new icon set")
        self.actions.add_task("Design Special Offer screen")

if __name__ == "__main__":
    app = App()
    app.mainloop()