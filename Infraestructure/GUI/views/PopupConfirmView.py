"""
FelipedelosH
2025
"""
import tkinter as tk
from Infraestructure.GUI.Screen import Screen

class PopupConfirmView(Screen):
    def __init__(self, master, manager, message, title="Mensaje"):
        self.master = master
        self.manager = manager
        self.message = message
        self.title = title
        self.result = None
        self.window = None

    def render(self, width, height):
        self.window = tk.Toplevel(self.master)
        self.window.title(self.title)
        self.window.geometry(f"{width}x{height}")
        self.window.resizable(False, False)

        lblMsg = tk.Label(self.window, text=self.message, wraplength=width - 50, justify="left")
        lblMsg.place(x=25, y=40)

        btnYes = tk.Button(self.window, text="Sí", width=10, command=self._on_yes)
        btnYes.place(x=width/2 - 80, y=height - 70)

        btnNo = tk.Button(self.window, text="No", width=10, command=self._on_no)
        btnNo.place(x=width/2 + 10, y=height - 70)

        self.window.grab_set()
        self.window.wait_window()

        return self.result

    def _on_yes(self):
        self.result = True
        self.window.destroy()

    def _on_no(self):
        self.result = False
        self.window.destroy()