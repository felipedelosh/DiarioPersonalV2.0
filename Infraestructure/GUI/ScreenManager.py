"""
FelipedelosH
2025
"""
class ScreenManager:
    def __init__(self, root):
        self.root = root
        self.screens = {}
        self.current_screen = None

    def add(self, name, screen_class):
        self.screens[name] = screen_class(self.root, self)

    def show(self, name):
        if self.current_screen:
            self.current_screen.destroy()
        self.current_screen = self.screens[name]
        self.current_screen.render()
