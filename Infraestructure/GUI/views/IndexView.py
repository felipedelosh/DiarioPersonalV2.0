"""
FelipedelosH
2025
"""
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
        lblCurrentDate = tk.Label(self.canvas, text=time_util.getTimeStamp())
        lblCurrentDate.place(x=_w*0.1, y=_h*0.25)
        lblMainMessage = tk.Label(self.canvas, text="Mensaje.")
        lblLastUsages = tk.Label(self.canvas, text="Esto casi no se usa.")
