import tkinter as tk
from tkinter import ttk
from Infraestructure.GUI.Screen import Screen


class PopupDateInputView(Screen):
    def __init__(self, master, timeController, manager, message, title="Seleccionar fecha"):
        self.master = master
        self.timeController = timeController
        self.manager = manager
        self.message = message
        self.title = title

        self.result = None
        self.window = None

        self.year_var = None
        self.month_var = None
        self.day_var = None

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

        years = [str(year) for year in self.timeController.getRangeOfYYYYFromXXToCurrentYYYY()]
        months = [f"{month:02d}" for month in self.timeController.getRangeOfAllMMOfYearInNumber()]
        days = [f"{day:02d}" for day in range(1, 32)]

        self.year_var = tk.StringVar(value="2025")
        self.month_var = tk.StringVar(value="01")
        self.day_var = tk.StringVar(value="01")

        cmbYear = ttk.Combobox(
            self.window,
            textvariable=self.year_var,
            values=years,
            state="readonly",
            width=10
        )
        cmbYear.place(x=width / 2 - 140, y=height / 2 - 10)

        cmbMonth = ttk.Combobox(
            self.window,
            textvariable=self.month_var,
            values=months,
            state="readonly",
            width=5
        )
        cmbMonth.place(x=width / 2 - 20, y=height / 2 - 10)

        cmbDay = ttk.Combobox(
            self.window,
            textvariable=self.day_var,
            values=days,
            state="readonly",
            width=5
        )
        cmbDay.place(x=width / 2 + 70, y=height / 2 - 10)

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
        year = self.year_var.get().strip()
        month = self.month_var.get().strip()
        day = self.day_var.get().strip()

        self.result = f"{year}/{month}/{day}"
        self.window.destroy()

    def _on_cancel(self):
        self.result = None
        self.window.destroy()
