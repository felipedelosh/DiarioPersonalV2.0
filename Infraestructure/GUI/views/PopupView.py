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

    def render(self, x, y):
        self.window = tk.Toplevel(self.master)
        self.window.title(self.title)
        self.window.geometry(f"{x}x{y}")
        self.window.resizable(False, False)

        Message = tk.Text(self.window, width=55, height=13, wrap="word")
        Message.insert(tk.END, self.message)
        Message.place(x=25, y=20)

        btnOk = tk.Button(self.window, text="OK", command=self.window.destroy)
        btnOk.place(x=222, y=260)

    def destroy(self):
        if self.window:
            self.window.destroy()
            self.window = None
