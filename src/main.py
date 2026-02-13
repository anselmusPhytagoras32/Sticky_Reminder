import contextlib
from datetime import date
import customtkinter as ctk
import ctypes
from modules.actions import Actions

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")  

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.overrideredirect(True) # Remove title bar
        self.title("To do")
        self.geometry("300x400")
        self.resizable(False, False)

        self.colors = {
            "bg_body": "#422e42",
            "bg_header": "#563e56", 
            "accent": "#bba151"
        }
        self.configure(fg_color=self.colors["bg_body"])

        # Dragging logic
        self.bind("<ButtonPress-1>", self.start_move)
        self.bind("<B1-Motion>", self.do_move)

        # Header
        self.header = ctk.CTkFrame(self, fg_color=self.colors["bg_header"], height=100, corner_radius=0)
        self.header.pack(fill="x", side="top")

        self.header.columnconfigure(0, weight=1) 
        self.header.columnconfigure(2, weight=2) 
        self.header.columnconfigure(3, weight=0) 
        self.header.columnconfigure(4, weight=0) 

        self.now = date.today()
        self.date_str = self.now.strftime("%d %B, %A")

        self.date_lbl = ctk.CTkLabel(self.header, text=self.date_str, font=("Helvetica", 14, "bold"), text_color="white")
        self.date_lbl.grid(row=0, column=2, sticky="s", pady=(10, 0))
        
        self.count_lbl = ctk.CTkLabel(self.header, text="0 tasks", font=("Helvetica", 12), text_color=self.colors["accent"])
        self.count_lbl.grid(row=1, column=2, sticky="n")

        # Minimize Button
        self.minimize_btn = ctk.CTkButton(
            self.header, text="-", font=("Arial", 20, "bold"), width=40, height=40,
            fg_color="transparent", text_color="white", hover_color="#6b4e6b",
            command=self.minimize_app
        )
        self.minimize_btn.grid(row=0, column=3, sticky="ne", padx=(0, 0), pady=10)

        # Close Button
        self.close_btn = ctk.CTkButton(
            self.header, text="×", font=("Arial", 20), width=40, height=40,
            fg_color="transparent", text_color="white", hover_color="#c42b1c",
            command=self.destroy
        )
        self.close_btn.grid(row=0, column=4, sticky="ne", padx=10, pady=10)

        # Main logic initialization (tasks list created here)
        self.tasks = []
        self.actions = Actions(self) # This triggers load_tasks()

        self.after(10, self.show_taskbar_icon)

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def do_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.winfo_x() + deltax
        y = self.winfo_y() + deltay
        self.geometry(f"+{x}+{y}")

    def show_taskbar_icon(self):
        with contextlib.suppress(Exception):
            GWL_EXSTYLE = -20
            WS_EX_APPWINDOW = 0x00040000
            WS_EX_TOOLWINDOW = 0x00000080
            hwnd = ctypes.windll.user32.GetParent(self.winfo_id())
            style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
            style = style & ~WS_EX_TOOLWINDOW
            style = style | WS_EX_APPWINDOW
            ctypes.windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, style)
            self.withdraw()
            self.after(10, self.deiconify)

    def minimize_app(self):
        self.withdraw()
        self.overrideredirect(False)
        self.iconify()
        self.bind("<Map>", self.restore_app)

    def restore_app(self, event):
        self.overrideredirect(True)
        self.unbind("<Map>")
        self.show_taskbar_icon()

if __name__ == "__main__":
    app = App()
    app.mainloop()