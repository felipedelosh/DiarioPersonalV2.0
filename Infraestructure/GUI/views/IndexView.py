"""
FelipedelosH
2025
"""
from Infraestructure.GUI.Screen import Screen

class IndexView(Screen):
    def render(self, x, y):
        self.canvas["bg"]="blue"
        self.canvas.place(x=x, y=y)
