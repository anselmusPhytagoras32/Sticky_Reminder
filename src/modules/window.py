import tkinter as tk
from modules import button
from modules.fields import InputField

def app_window():
    window = tk.Tk()

    window.title("To do")
    window.minsize(400, 500)
    window.maxsize(500, 500)
    window.geometry("350x350")
    tk.Label(window, text = "To do: ").pack()
    
    main_frame = tk.Frame(window)
    main_frame.pack(expand=True, fill="both", padx=2, pady=20)

    take_input = InputField(main_frame)
    take_input.add_queue()
        
    button.delete_button(main_frame)
    button.edit_button(main_frame)
    button.add_button(main_frame, take_input)
    
    window.mainloop()