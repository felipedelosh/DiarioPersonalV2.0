"""
FelipedelosH
2025
"""
from Infraestructure.GUI.Screen import Screen

class FinancesView(Screen):
    def render(self, x, y):
        self.canvas["bg"]="yellow"
        self.canvas.place(x=x, y=y)
        self._w = float(self.canvas["width"])
        self._h =float(self.canvas["height"])
        self.lang = self.manager.controller.dependencies["lang"]
        self.usageService = self.manager.controller.dependencies["usage_service"]
        _options = self.lang.getText("economy_options")

        self.renderButons(_options, self._w, self._h)

    def renderButons(self, _options, _w, _h):
        pass
