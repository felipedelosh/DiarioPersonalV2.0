"""
FelipedelosH
2025
"""
import tkinter as tk
from Infraestructure.GUI.Screen import Screen

class SettingsView(Screen):
    def render(self, x, y):
        self.canvas["bg"]="cyan"
        self.canvas.place(x=x, y=y)
        self._w = float(self.canvas["width"])
        self._h =float(self.canvas["height"])
        self.btns = []
        self._tempCurrentElementsOptions = [] # TO DELETE AFTER USE OR CHANGE VIEW
        self.lang = self.manager.controller.dependencies["lang"]
        lblTitle = tk.Label(self.canvas, text=self.lang.getText("settings_title"))
        lblTitle.place(x=self._w*0.38, y=self._h*0.05)
        _options = self.lang.getText("settings_options")
        self.renderButons(_options, self._w, self._h)

    def renderButons(self, _options, _w, _h):
        _total_butons = len(_options)

        if _total_butons == 0:
            return
    
        if _total_butons > 0:
            _total_btns_w = 0
            for i in _options:
                btn = tk.Button(self.canvas, text=i, command=lambda opt=i: self.drawBtnInterface(_options, opt))
                self.btns.append(btn)

        btn_height = self.btns[0].winfo_reqheight()
        spacing = btn_height * 0.5
        total_height = _total_butons * btn_height + (_total_butons - 1) * spacing
        start_y = (_h - total_height) / 2

        for idx, btn in enumerate(self.btns):
            btn_width = btn.winfo_reqwidth()
            x_pos = (_w - btn_width) / 2
            y_pos = start_y + idx * (btn_height + spacing)
            btn.place(x=x_pos, y=y_pos)

    def drawBtnInterface(self, _options, opt):
        if opt == _options[0]:
            pass
        elif opt == _options[1]:
            pass
        elif opt == _options[2]:
            pass
        elif opt == _options[3]:
            pass
        elif opt == _options[4]:
            pass
        elif opt == _options[5]:
            pass
        elif opt == _options[6]:
            pass
        elif opt == _options[7]:
            pass
