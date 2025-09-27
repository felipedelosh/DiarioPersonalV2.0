"""
FelipedelosH
2025
"""
from Infraestructure.GUI.Screen import Screen

class ChatbotView(Screen):
    def render(self, x, y):
        self.canvas["bg"]="black"
        self.canvas.place(x=x, y=y)
