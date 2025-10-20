"""
FelipedelosH
2025
"""
import tkinter as tk
from tkinter import ttk as ttk
from Infraestructure.GUI.Screen import Screen

class FinancesView(Screen):
    def render(self, x, y):
        self.canvas["bg"]="yellow"
        self.canvas.place(x=x, y=y)
        self._w = float(self.canvas["width"])
        self._h =float(self.canvas["height"])
        self.btns = []
        self._tempCurrentElementsOptions = [] # TO DELETE AFTER USE OR CHANGE VIEW
        self.lang = self.manager.controller.dependencies["lang"]
        self.usageService = self.manager.controller.dependencies["usage_service"]
        lblTitle = tk.Label(self.canvas, text=self.lang.getText("economy_title"))
        lblTitle.place(x=self._w*0.38, y=self._h*0.05)
        _options = self.lang.getText("economy_options")
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
                btn.place(x=current_x, y=_h * 0.18)
                current_x += btn.winfo_reqwidth() + _spacing

    def drawBtnInterface(self, _options, opt):
        if opt == _options[0]:
            self.deleteOption()
            self.drawTAccountOption()
        if opt == _options[1]:
            self.deleteOption()
            print("Trabajo")
        if opt == _options[2]:
            self.deleteOption()
            print("Ahorros")
        if opt == _options[3]:
            self.deleteOption()
            print("Deudas y Compromisos")
        if opt == _options[4]:
            self.deleteOption()
            print("Resumenes")
        if opt == _options[5]:
            self.deleteOption()
            print("Buscar")

    def deleteOption(self):
        for widget in self._tempCurrentElementsOptions:
            widget.destroy()
        self._tempCurrentElementsOptions.clear()

    # T ACCOUNTS
    def drawTAccountOption(self):
        _itemsDiplayed = 10
        _concepts = []
        _debits = []
        _credits = []
        _hplus = 0.27
        _h = self._h - (self._h * _hplus)
        _dh = (_h / _itemsDiplayed) * 0.75
        lblConcept = tk.Label(self.canvas, text=self.lang.getText("economy_concept"))
        self._tempCurrentElementsOptions.append(lblConcept)
        lblConcept.place(x=self._w * 0.22, y=self._h * 0.27)
        lblDebit = tk.Label(self.canvas, text=self.lang.getText("economy_debit"))
        self._tempCurrentElementsOptions.append(lblDebit)
        lblDebit.place(x=self._w * 0.56, y=self._h * 0.27)
        lblCredit = tk.Label(self.canvas, text=self.lang.getText("economy_credit"))
        self._tempCurrentElementsOptions.append(lblCredit)
        lblCredit.place(x=self._w * 0.8, y=self._h * 0.27)
        lblday = tk.Label(self.canvas, text=self.lang.getText("econimy_day"))
        self._tempCurrentElementsOptions.append(lblday)
        lblday.place(x=self._w * 0.1, y=self._h * 0.9)
        # WIP


        cmbxNrDays = ttk.Combobox(self.canvas, state='readonly')
        self._tempCurrentElementsOptions.append(cmbxNrDays)


        for i in range(_itemsDiplayed):
            lblIndex = tk.Label(self.canvas, text=str(i+1) + " :")
            self._tempCurrentElementsOptions.append(lblIndex)
            _y = ((self._h * _hplus) + (_dh * (i + 1)))
            lblIndex.place(x=self._w * 0.03, y=_y)
            txtConcept = tk.Entry(self.canvas, width=40)
            self._tempCurrentElementsOptions.append(txtConcept)
            _concepts.append(txtConcept)
            _concepts[i].place(x=self._w * 0.09, y=_y)
            txtDebit = tk.Entry(self.canvas, width=22)
            self._tempCurrentElementsOptions.append(txtDebit)
            _debits.append(txtDebit)
            _debits[i].place(x=self._w * 0.5, y=_y)
            txtCredit = tk.Entry(self.canvas, width=22)
            self._tempCurrentElementsOptions.append(txtCredit)
            _credits.append(txtCredit)
            _credits[i].place(x=self._w * 0.75, y=_y)


    # T ACCOUNTS

