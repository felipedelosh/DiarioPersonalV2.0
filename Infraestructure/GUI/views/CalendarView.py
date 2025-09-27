"""
FelipedelosH
2025
"""
from Infraestructure.GUI.Screen import Screen

class CalendarView(Screen):
    def render(self, x, y):
        self.canvas["bg"]="red"
        self.canvas.place(x=x, y=y)
