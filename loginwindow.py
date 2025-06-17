import tkinter as tk
from tkinter import ttk
from gui.main_window import MainWindow

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("InstaCampus Login")
        self.root.geometry("300x200")

        ttk.Label(root, text="Welcome to InstaCampus!", font=("Helvetica", 14)).pack(pady=20)

        ttk.Label(root, text="Enter your username:").pack()
        self.username_entry = ttk.Entry(root, width=25)
        self.username_entry.pack(pady=10)

        ttk.Button(root, text="Login", command=self.login).pack()

    def login(self):
        username = self.username_entry.get().strip()
        if username:
            self.root.destroy()  # Close login window

            # Open main window
            main_root = tk.Tk()
            app = MainWindow(main_root, username=username)
            main_root.mainloop()