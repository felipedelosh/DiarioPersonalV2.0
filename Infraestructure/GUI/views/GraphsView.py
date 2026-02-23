"""
FelipedelosH
2025
"""
import tkinter as tk
from Infraestructure.GUI.Screen import Screen


class GraphsView(Screen):
    def render(self, x, y):
        self.canvas["bg"]="snow"
        self.canvas.place(x=x, y=y)
        self._w = float(self.canvas["width"])
        self._h =float(self.canvas["height"])
        self.lang = self.manager.controller.dependencies["lang"]
        self._tempCurrentElementsOptions = [] # TO DELETE AFTER USE OR CHANGE VIEW
        self.btns = []
        _options = self.lang.getText("graphics_options")
        lblTitle = tk.Label(self.canvas, text=self.lang.getText("graphics_title_message"))
        lblTitle.place(x=self._w*0.4, y=self._h*0.05)
        self.renderButons(_options, self._w, self._h)

    def renderButons(self, _options, _w, _h):
        _total_butons = len(_options)
        if _total_butons > 0:
            _total_btns_w = 0
            for i in _options:
                btn = tk.Button(self.canvas, text=i, command=lambda opt=i: self.drawBtnInterface(_options, opt))
                _total_btns_w = _total_btns_w + btn.winfo_reqwidth()
                self.btns.append(btn)

            _space_free = _w - _total_btns_w
            _spacing = _space_free / (_total_butons + 1)
            current_x = _spacing
            for btn in self.btns:
                btn.place(x=current_x, y=_h * 0.12)
                current_x += btn.winfo_reqwidth() + _spacing
    def drawBtnInterface(self, _options, opt):
        if opt == _options[0]:
            self.deleteOption()
            self.drawEconomyGraphicsOptions()
        if opt == _options[1]:
            self.deleteOption()
            self.drawFeelsGraphicsOptions()
        if opt == _options[2]:
            self.deleteOption()
            self.drawDrugsGraphicsOptions()
        if opt == _options[3]:
            self.deleteOption()
            self.drawTimeGraphicsOptions()
            
    # Economy
    def drawEconomyGraphicsOptions(self):
        print("Economía")
    # Economy

    # Feelings
    def drawFeelsGraphicsOptions(self):
        print("Sentimientos")
    # Feelings

    # Drugs
    def drawDrugsGraphicsOptions(self):
        print("Drogas")
    # Drugs

    # Time
    def drawTimeGraphicsOptions(self):
        print("Tiempo")
    # Time

    def deleteOption(self):
        for widget in self._tempCurrentElementsOptions:
            widget.destroy()
        self._tempCurrentElementsOptions.clear()
