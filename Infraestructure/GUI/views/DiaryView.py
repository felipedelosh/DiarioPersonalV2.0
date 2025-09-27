"""
FelipedelosH
2025
"""
from Infraestructure.GUI.Screen import Screen

class DiaryView(Screen):
    def render(self, x, y):
        self.canvas["bg"]="purple"
        self.canvas.place(x=x, y=y)
