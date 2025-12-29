"""
FelipedelosH
2025
"""
import tkinter as tk
from Infraestructure.GUI.Screen import Screen

class PopupInputView(Screen):
    def __init__(self, master, manager, message, title="Entrada de dato", input_type="text"):
        """
        input_type: "text" | "number"
        """
        self.master = master
        self.manager = manager
        self.message = message
        self.title = title
        self.input_type = input_type
        self.result = None
        self.window = None
        self._input_var = None

    def render(self, width, height):
        self.window = tk.Toplevel(self.master)
        self.window.title(self.title)
        self.window.geometry(f"{width}x{height}")
        self.window.resizable(False, False)

        lblMsg = tk.Label(
            self.window,
            text=self.message,
            wraplength=width - 40,
            justify="left"
        )
        lblMsg.place(x=20, y=30)

        self._input_var = tk.StringVar()

        entry = tk.Entry(
            self.window,
            textvariable=self._input_var,
            width=30
        )
        entry.place(x=width / 2 - 120, y=height / 2 - 10)
        entry.focus()

        btnCancel = tk.Button(
            self.window,
            text="Cancelar",
            width=10,
            command=self._on_cancel
        )
        btnCancel.place(x=width / 2 - 110, y=height - 60)

        btnOk = tk.Button(
            self.window,
            text="Aceptar",
            width=10,
            command=self._on_ok
        )
        btnOk.place(x=width / 2 + 20, y=height - 60)

        self.window.grab_set()
        self.window.wait_window()

        return self.result

    def _on_ok(self):
        value = self._input_var.get().strip()

        if self.input_type == "number":
            if not value.replace(".", "", 1).isdigit():
                return

        self.result = value
        self.window.destroy()

    def _on_cancel(self):
        self.result = None
        self.window.destroy()
