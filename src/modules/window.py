import tkinter as tk

def app_window():
    window = tk.Tk()
    window.title("To do")
    window.minsize(200, 300)
    window.maxsize(300, 500)
    window.geometry("300x300+50+50")
    tk.Label(window, text = "To do: ").pack()

    window.mainloop()