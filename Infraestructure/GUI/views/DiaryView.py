"""
FelipedelosH
2025
"""
import tkinter as tk
from Infraestructure.GUI.Screen import Screen

class DiaryView(Screen):
    def render(self, x, y):
        self.canvas["bg"]="purple"
        self.canvas.place(x=x, y=y)
        _w = float(self.canvas["width"])
        _h =float(self.canvas["height"])
        lang = self.manager.controller.dependencies["lang"]
        self.btns = []
        _options = lang.getText("diary_options")
        lblTitle = tk.Label(self.canvas, text=lang.getText("diary_title_message"))
        lblTitle.place(x=_w*0.4, y=_h*0.05)
        self.renderButons(_options, _w, _h)

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
                btn.place(x=current_x, y=_h * 0.18)
                current_x += btn.winfo_reqwidth() + _spacing

    def drawBtnInterface(self, _options, opt):
        if opt == _options[0]:
            print("Diario")
        if opt == _options[1]:
            print("Sueños")
        if opt == _options[2]:
            print("Amigos")
        if opt == _options[3]:
            print("Notas")
        if opt == _options[4]:
            print("Registro de Sentimientos")
        if opt == _options[5]:
            print("Drogas")
