"""
FelipedelosH
2025
"""
import tkinter as tk
from Infraestructure.GUI.Screen import Screen

class PopupView(Screen):
    def __init__(self, master, manager, message, title="Mensaje"):
        self.master = master
        self.manager = manager
        self.message = message
        self.title = title
        self.window = None

    def render(self, x=100, y=100):
        self.window = tk.Toplevel(self.master)
        self.window.title(self.title)
        self.window.geometry("300x150+%d+%d" % (x, y))
        self.window.resizable(False, False)

        lblMessage = tk.Label(self.window, text=self.message, fg="red", font=("Arial", 12))
        lblMessage.pack(pady=20)

        btnOk = tk.Button(self.window, text="OK", command=self.window.destroy)
        btnOk.pack(pady=10)

    def destroy(self):
        if self.window:
            self.window.destroy()
            self.window = None
