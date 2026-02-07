import tkinter as tk

def init_window():
    window = tk.Tk()
    window.title("To do")
    window.minsize(200, 300)
    window.maxsize(300, 500)
    window.mainloop()