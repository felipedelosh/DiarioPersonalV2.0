"""
FelipedelosH
2025
"""
from Infraestructure.GUI.Screen import Screen

class FinancesView(Screen):
    def render(self, x, y):
        self.canvas["bg"]="yellow"
        self.canvas.place(x=x, y=y)
        _w = float(self.canvas["width"])
        _h =float(self.canvas["height"])