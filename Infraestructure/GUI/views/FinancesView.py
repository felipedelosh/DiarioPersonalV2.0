"""
FelipedelosH
2025
"""
import tkinter as tk
from tkinter import ttk as ttk
from Infraestructure.GUI.Screen import Screen
from Infraestructure.GUI.views.PopupView import PopupView

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
        lblday = tk.Label(self.canvas, text=self.lang.getText("economy_day"))
        self._tempCurrentElementsOptions.append(lblday)
        lblday.place(x=self._w * 0.1, y=self._h * 0.9)
        _currentDD = self.manager.controller.utils["time_util"].getCurrentDD()
        _currentMM = self.manager.controller.utils["time_util"].getCurrentMM()
        cmbxNrDays = ttk.Combobox(self.canvas, state='readonly', width=4)
        self._tempCurrentElementsOptions.append(cmbxNrDays)
        cmbxNrDays['values'] = [x for x in range(1, self.manager.controller.utils["time_util"].getNumberOfDaysInXMM(_currentMM - 1) + 1)]
        cmbxNrDays.current(_currentDD)
        cmbxNrDays.place(x=self._w * 0.15, y=self._h * 0.9)
        lblMonth = tk.Label(self.canvas, text=self.lang.getText("economy_month"))
        self._tempCurrentElementsOptions.append(lblMonth)
        lblMonth.place(x=self._w * 0.25, y=self._h * 0.9)
        cmbxNrMonth = ttk.Combobox(self.canvas, state='readonly', width=4)
        self._tempCurrentElementsOptions.append(cmbxNrMonth)
        cmbxNrMonth['values'] = [x for x in range(1, _currentMM + 1)]
        cmbxNrMonth.current(_currentMM - 1)
        cmbxNrMonth.place(x=self._w * 0.3, y=self._h * 0.9)

        btnSaveTAccount = tk.Button(self.canvas, text=self.lang.getText("text_button_save"), command=lambda: self.saveTAccounts(_itemsDiplayed, _concepts, _debits, _credits))
        self._tempCurrentElementsOptions.append(btnSaveTAccount)
        btnSaveTAccount.place(x=self._w * 0.66, y=self._h * 0.89)

        btnLoadTAccount = tk.Button(self.canvas, text=self.lang.getText("text_button_load"))
        self._tempCurrentElementsOptions.append(btnLoadTAccount)
        btnLoadTAccount.place(x=self._w * 0.76, y=self._h * 0.89)
        
        btnSerachTAccount = tk.Button(self.canvas, text=self.lang.getText("text_button_load"))
        self._tempCurrentElementsOptions.append(btnSerachTAccount)
        btnSerachTAccount.place(x=self._w * 0.86, y=self._h * 0.89)

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

    def saveTAccounts(self, itemsDiplayed, concepts, debits, credits):
        _errorCounter = 0
        _isSomeData = False
        _tAccountData = ""
        for i in range(itemsDiplayed):
            _itterConcep = concepts[i].get()
            _itterDebit = debits[i].get()
            _itterCredit = credits[i].get()

            if not self._isTAccountsReportValid(_itterConcep, _itterDebit, _itterCredit):
                _errorCounter = _errorCounter + 1
                concepts[i]["bg"] = "red"
                debits[i]["bg"] = "red"
                credits[i]["bg"] = "red"
            else:
                concepts[i]["bg"] = "white"
                debits[i]["bg"] = "white"
                credits[i]["bg"] = "white"

                if str(_itterConcep).strip() == "":
                    continue

                if str(_itterDebit).strip() == "":
                    _itterDebit = 0

                if str(_itterCredit).strip() == "":
                    _itterCredit = 0

                _isSomeData = True
                _tAccountData = _tAccountData + f"{_itterConcep};{_itterDebit};{_itterCredit}\n"           

        if _errorCounter > 0:
            PopupView(self.master, self.manager, self.lang.getText("error_economy_report_save"), "ERROR").render(500, 300)
            return
        
        if not _isSomeData:
            PopupView(self.master, self.manager, self.lang.getText("error_economy_report_save_no_info"), "ERROR").render(500, 300)
            return
        
        # SAVE TAccount
        if _isSomeData:
            _path = self.manager.controller.pathController.getPathByCODE("ECONOMY_TACCOUNTS_CURRENT_YYYY")
            _currentMonth = self.manager.controller.utils["time_util"].getCurrentMM()
            _currentMonth = self.lang.getText("month_names")[_currentMonth - 1]
            _currentDay = self.manager.controller.utils["time_util"].getCurrentDD()
            _path = f"{_path}{_currentMonth} {_currentDay}.csv"

            data = _tAccountData[:-1] # Delete last break line.

            _status = self.manager.controller.dependencies["economy_use_case_save_taccount"].execute(_path, data)

            if _status:
                PopupView(self.master, self.manager, self.lang.getText("ok_economy_save_report"), "SAVE").render(500, 300)
                _path = self.manager.controller.pathController.getPathByCODE("USAGES")
                _path = f"{_path}\\{self.manager.controller.utils["time_util"].getCurrentYYYY()}-economy.txt"
                _data = f"{self.manager.controller.utils["time_util"].getTimeStamp()} {self.manager.controller.utils["time_util"].getCurrentHHMMSS()}"
                self.usageService.save_usage(_path, _data)
                
                # Clear VIEW
                
            else:
                PopupView(self.master, self.manager, self.lang.getText("error_diary_page_save"), "ERROR").render(500, 300)
                return


    def _isTAccountsReportValid(self, concept, debit, credit):
        try:
            if str(concept).strip() == "" and str(debit).strip() == "" and str(credit).strip() == "":
                return True
            
            if str(concept).strip() != "" and str(debit).strip() == "" and str(credit).strip() == "":
                return False
            
            if str(debit).strip() != "" and str(credit).strip() != "":
                return False
        
            if str(concept).strip() == "" and (str(debit).strip() != "" or str(credit).strip() != ""):
                return False
            
            if str(debit).strip() != "":
                if int(debit) < 0:
                    return False
            
            if str(credit).strip() != "":
                if int(credit) < 0:
                    return False
            
            return True
        except:
            return False
    # T ACCOUNTS
