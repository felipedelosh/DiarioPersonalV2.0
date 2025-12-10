"""
FelipedelosH
2025
"""
import tkinter as tk
from tkinter import ttk as ttk
from Infraestructure.GUI.Screen import Screen
from Infraestructure.GUI.views.PopupView import PopupView

class CalendarView(Screen):
    def render(self, x, y):
        self.canvas["bg"]="red"
        self.canvas.place(x=x, y=y)
        self._w = float(self.canvas["width"])
        self._h =float(self.canvas["height"])
        self.btns = []
        self.lang = self.manager.controller.dependencies["lang"]
        self._tempCurrentElementsOptions = [] # TO DELETE AFTER USE OR CHANGE VIEW
        lblTitle = tk.Label(self.canvas, text=self.lang.getText("schelude_title"))
        lblTitle.place(x=self._w*0.38, y=self._h*0.05)
        _options = self.lang.getText("schelude_options")
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
            print("Calendario")
        if opt == _options[1]:
            self.deleteOption()
            self.draw24HOption()
        if opt == _options[2]:
            self.deleteOption()
            print("Horario")
    def deleteOption(self):
        for widget in self._tempCurrentElementsOptions:
            widget.destroy()
        self._tempCurrentElementsOptions.clear()

    #24H
    def draw24HOption(self):
        lblTitleSchelude = tk.Label(self.canvas, text=self.lang.getText("title_schelude"))
        self._tempCurrentElementsOptions.append(lblTitleSchelude)
        lblTitleSchelude.place(x=self._w*0.37, y=self._h*0.3)
        lblHelpSchelude = tk.Label(self.canvas, text=self.lang.getText("help_schelude"))
        self._tempCurrentElementsOptions.append(lblHelpSchelude)
        lblHelpSchelude.place(x=self._w*0.28, y=self._h*0.36)
        _24HrsRegisterArr = []

        # Display 24Hrs in 3 Groups of 8 Hours
        H = self._h * 0.44
        X = self._w * 0.9
        dh = (H / 7) * 0.8
        dx = X / 3

        _counterH = 0
        _counterX = 0
        for itterHH in range(24):
            _HH_ = self.manager.controller.utils["time_util"].getStrHHByCounter(6, itterHH)
            lblHour = tk.Label(self.canvas, text=_HH_)
            self._tempCurrentElementsOptions.append(lblHour)
            lblHour.place(x=self._w * 0.07 + (dx * _counterX), y=H + (dh * _counterH))

            cmbxHHReg = ttk.Combobox(self.canvas, state='readonly', width=18)
            self._tempCurrentElementsOptions.append(cmbxHHReg)
            cmbxHHReg['values'] = self.lang.getText("schelude_24h_options")
            _24HrsRegisterArr.append(cmbxHHReg)
            _24HrsRegisterArr[itterHH].place(x=self._w * 0.15 + (dx * _counterX), y=H + (dh * _counterH))

            _counterH = _counterH + 1
            if _counterH == 8 or _counterH == 16:
                _counterH = 0
                _counterX = _counterX + 1

        btnSave24Hrs = tk.Button(self.canvas, text=self.lang.getText("text_button_save"), command=lambda :self._save24HReport(_24HrsRegisterArr))
        self._tempCurrentElementsOptions.append(btnSave24Hrs)
        btnSave24Hrs.place(x=self._w * 0.44, y=self._h * 0.87)

    def _save24HReport(self, reg24hArr):
        _counter = 0
        _errs = 0

        _dataToSave = ""
        for itterHH in reg24hArr:
            _HH = self.manager.controller.utils["time_util"].getStrHHByCounter(6, _counter)
            _act = itterHH.get()

            if str(_act).strip() == "":
                _errs = _errs + 1
                continue

            _dataToSave = _dataToSave + f"{_HH}:{_act}" + "\n"

            _counter = _counter + 1

        if not _errs:
            _path = self.manager.controller.pathController.getPathByCODE("SCHELUDED_24_H_CURRENT_YYYY")
            _filename = f"{self.manager.controller.utils["time_util"].getTimeStamp()}.txt"

            _reqSave24H = self.manager.controller.dependencies["schedule_use_case_save_24h_report"].execute(f"{_path}{_filename}", _dataToSave)
            if _reqSave24H:
                PopupView(self.master, self.manager, self.lang.getText("text_ok_to_save"), "SAVE").render(500, 300)
                _path = self.manager.controller.pathController.getPathByCODE("USAGES")
                YYYY = self.manager.controller.utils["time_util"].getCurrentYYYY()
                typeUsage = "24h"
                timeStamp = f"{self.manager.controller.utils["time_util"].getTimeStamp()} {self.manager.controller.utils["time_util"].getCurrentHHMMSS()}"
                
                self.manager.controller.dependencies["usage_use_case_save"].execute(_path, YYYY, typeUsage, timeStamp)
                self._clear24HAfterOkSave(reg24hArr)
            else:
                PopupView(self.master, self.manager, self.lang.getText("error_schedule_save_error"), "ERROR").render(500, 300)
        else:
            PopupView(self.master, self.manager, self.lang.getText("error_schelude_missing_fields"), "ERROR").render(500, 300)
    def _clear24HAfterOkSave(self, _24HrsRegisterArr):
        for itterHH in _24HrsRegisterArr:
            itterHH.set("")
    #24H