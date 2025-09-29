# ScreenManager.py
"""
FelipedelosH
2025
"""
class ScreenManager:
    def __init__(self, root, sideBar_canvas, content_canvas, controller):
        self.root = root
        self.sideBar = sideBar_canvas
        self.content = content_canvas
        self.controller = controller
        self._screen_classes = {}
        self.current_screen = None
        self.current_name = None

    def add(self, name, screen_class):
        self._screen_classes[name] = screen_class

    def show(self, name, x, y):
        screen_class = self._screen_classes.get(name)
        if not screen_class:
            raise ValueError(f"No existe la pantalla '{name}' registrada.")

        for widget in self.content.winfo_children():
            widget.destroy()

        if self.current_screen is not None:
            try:
                self.current_screen.destroy()
            except Exception:
                pass
            self.current_screen = None
            self.current_name = None

        self.current_screen = screen_class(self.root, self.content, self)
        self.current_name = name
        self.current_screen.render(x, y)
