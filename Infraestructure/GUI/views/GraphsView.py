"""
FelipedelosH
2025
"""
from Infraestructure.GUI.Screen import Screen

class GraphsView(Screen):
    def render(self, x, y):
        self.canvas["bg"]="snow"
        self.canvas.place(x=x, y=y)
