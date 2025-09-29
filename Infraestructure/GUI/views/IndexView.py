"""
FelipedelosH
2025
"""
import random
import tkinter as tk
from Infraestructure.GUI.Screen import Screen

class IndexView(Screen):
    def render(self, x, y):
        self.canvas.place(x=x, y=y)
        _w = float(self.canvas["width"])
        _h =float(self.canvas["height"])

        lang = self.manager.controller.dependencies["lang"]
        time_util = self.manager.controller.utils["time_util"]
        lblTile = tk.Label(self.canvas, text=lang.getText("welcome_message"))
        lblTile.place(x=_w*0.4, y=_h*0.05)
        _currentDayName = lang.getText("days_names")[time_util.getNumberOfCurrentDD()]
        _currentMonthName = lang.getText("month_names")[time_util.getCurrentMM()-1]
        _txtDateToday = f"{_currentDayName}, {time_util.getCurrentDD()} - {_currentMonthName} - {time_util.getCurrentYYYY()}".upper()
        lblCurrentDate = tk.Label(self.canvas, text=_txtDateToday)
        lblCurrentDate.place(x=_w*0.1, y=_h*0.15)
        _motivational_message = random.choice(lang.getText("motivational_message"))
        lblMainMessage = tk.Label(self.canvas, text=_motivational_message)
        lblMainMessage.place(x=_w*0.1, y=_h*0.2)
        lblLastUsages = tk.Label(self.canvas, text="Esto casi no se usa.")
