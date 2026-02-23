"""
FelipedelosH
2025
"""
import tkinter as tk
from tkinter import ttk as ttk
from Infraestructure.GUI.Screen import Screen
from Infraestructure.GUI.views.PopupView import PopupView


class GraphsView(Screen):
    def render(self, x, y):
        self.canvas["bg"]="snow"
        self.canvas.place(x=x, y=y)
        self._w = float(self.canvas["width"])
        self._h =float(self.canvas["height"])
        self.lang = self.manager.controller.dependencies["lang"]
        # PAINTED CANVAS
        self.auxiliarCanvas = tk.Canvas(self.canvas, bg="yellow")
        # END PAINTED CANVAS
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
        lblHelpFilterByEconomyGraphics = tk.Label(self.canvas, text=self.lang.getText("graphics_economy_help_filter_by_category"))
        self._tempCurrentElementsOptions.append(lblHelpFilterByEconomyGraphics)
        lblHelpFilterByEconomyGraphics.place(x=self._w * 0.05, y=self._h * 0.2)
        cmbxEconomyOptionsGraphicsFilter = ttk.Combobox(self.canvas, state='readonly', width=30)
        cmbxEconomyOptionsGraphicsFilter["values"] = self.lang.getText("graphics_economy_categories")
        self._tempCurrentElementsOptions.append(cmbxEconomyOptionsGraphicsFilter)
        cmbxEconomyOptionsGraphicsFilter.place(x=self._w * 0.35, y=self._h * 0.2)

        btnPaint = tk.Button(self.canvas, bg="green", text=self.lang.getText("text_button_graphic"), command=lambda: self.paintEconomy(cmbxEconomyOptionsGraphicsFilter.get()))
        self._tempCurrentElementsOptions.append(btnPaint)
        btnPaint.place(x=self._w * 0.45, y=self._h * 0.32)

    def paintEconomy(self, option):
        if option == self.lang.getText("graphics_economy_categories")[0]:
            self.paintedCanvas("PIE_TACCOUNTS")
        if option == self.lang.getText("graphics_economy_categories")[1]:
            self.paintedCanvas("BAR_TACCOUNTS")
        if option == self.lang.getText("graphics_economy_categories")[2]:
            self.paintedCanvas("BAR_FILTERED_TIME")
        if option == self.lang.getText("graphics_economy_categories")[3]:
            self.paintedCanvas("ZZZ_CATESIAN")
        if option == self.lang.getText("graphics_economy_categories")[4]:
            self.paintedCanvas("BAR_FILTERED_CATEGORY")
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

    def paintedCanvas(self, graphicsType):
        _data = None
        graphier = self.manager.controller.utils["graphics_renderder"]
        graphier.render(self.auxiliarCanvas, _data, graphicsType, None)
        self.auxiliarCanvas.place(x=self._w * 0.05, y=self._h * 0.40, width=self._w * 0.90, height=self._h * 0.55)

    def deleteOption(self):
        for widget in self._tempCurrentElementsOptions:
            widget.destroy()
        self._tempCurrentElementsOptions.clear()
