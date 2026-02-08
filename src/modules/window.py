import tkinter as tk
from modules import button

def app_window():
    window = tk.Tk()

    window.title("To do")
    window.minsize(200, 300)
    window.maxsize(300, 500)
    window.geometry("350x350")
    tk.Label(window, text = "To do: ").pack()
    
    main_frame = tk.Frame(window)
    main_frame.pack(expand=True, fill="both", pady=20)
    
    button.history_button(main_frame)
    button.add_button(main_frame)
    button.delete_button(main_frame)
    window.mainloop()