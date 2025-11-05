import tkinter as tk
import tkinter.ttk as ttk


def add_task():
    user_input = input("Enter a task: ")



    while True:
        print("Welcome to Sticky Reminder")
        print("Select operation to perform")
        print("1. Add a message")
        print("2. Remove a message")
        print("3. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()


