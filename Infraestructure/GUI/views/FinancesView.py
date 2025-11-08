"""
FelipedelosH
2025
"""
import tkinter as tk
from tkinter import ttk as ttk
from Infraestructure.GUI.Screen import Screen
from Infraestructure.GUI.views.PopupView import PopupView
from Infraestructure.GUI.views.PopupConfirmView import PopupConfirmView

class FinancesView(Screen):
    def render(self, x, y):
        self.canvas["bg"]="yellow"
        self.canvas.place(x=x, y=y)
        self._w = float(self.canvas["width"])
        self._h =float(self.canvas["height"])
        self.btns = []
        self._tempCurrentElementsOptions = [] # TO DELETE AFTER USE OR CHANGE VIEW
        self._tempDebitArrayItems = []
        self.lang = self.manager.controller.dependencies["lang"]
        self.usageService = self.manager.controller.dependencies["usage_service"]
        self.stringProcesor = self.manager.controller.utils["string_procesor"]
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
            self.drawDebitsOption()
        if opt == _options[4]:
            self.deleteOption()
            print("Resumenes")
        if opt == _options[5]:
            self.deleteOption()
            print("Buscar")

    def deleteOption(self):
        self.deleteDisplayedDrawOption()
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
        cmbxNrDays.current(_currentDD-1)
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

    # DEBITS
    def drawDebitsOption(self):
        self._tempDebitArrayItems = []
        btnNewDebit = tk.Button(self.canvas, text=self.lang.getText("debit_btn_new_debit"), command=lambda: self.drawNewDebit())
        self._tempCurrentElementsOptions.append(btnNewDebit)
        btnNewDebit.place(x=self._w * 0.26, y=self._h * 0.3)

        btnDebitPayment = tk.Button(self.canvas, text=self.lang.getText("debit_btn_debit_payment"), command=lambda: self.drawDebitPayments())
        self._tempCurrentElementsOptions.append(btnDebitPayment)
        btnDebitPayment.place(x=self._w * 0.42, y=self._h * 0.3)

        btnHistoryDebit = tk.Button(self.canvas, text=self.lang.getText("debit_btn_debit_history"), command=lambda: self.drawDebitHistory())
        self._tempCurrentElementsOptions.append(btnHistoryDebit)
        btnHistoryDebit.place(x=self._w * 0.6, y=self._h * 0.3)


    def drawNewDebit(self):
        self.deleteDisplayedDrawOption()

        lblDebitTile = tk.Label(self.canvas, text=self.lang.getText("debit_main_title"))
        self._tempDebitArrayItems.append(lblDebitTile)
        lblDebitTile.place(x=self._w * 0.06, y=self._h * 0.42)
        lblAmounth = tk.Label(self.canvas, text=self.lang.getText("debit_amount"))
        self._tempDebitArrayItems.append(lblAmounth)
        lblAmounth.place(x=self._w * 0.06, y=self._h * 0.47)
        txtAmounth = tk.Entry(self.canvas, width=15)
        self._tempDebitArrayItems.append(txtAmounth)
        txtAmounth.place(x=self._w * 0.14, y=self._h * 0.473)
        lblDebitInterest = tk.Label(self.canvas, text=self.lang.getText("debit_interest"))
        self._tempDebitArrayItems.append(lblDebitInterest)
        lblDebitInterest.place(x=self._w * 0.33, y=self._h * 0.47)
        txtDebitInterest = tk.Entry(self.canvas, width=6)
        self._tempDebitArrayItems.append(txtDebitInterest)
        txtDebitInterest.place(x=self._w * 0.46, y=self._h * 0.473)
        lblDeadLine = tk.Label(self.canvas, text=self.lang.getText("debit_deathline"))
        self._tempDebitArrayItems.append(lblDeadLine)
        lblDeadLine.place(x=self._w * 0.58, y=self._h * 0.47)
        txtDeadLine  = tk.Entry(self.canvas, width=18)
        self._tempDebitArrayItems.append(txtDeadLine)
        txtDeadLine.place(x=self._w * 0.77, y=self._h * 0.473) 
        lblDebitDescription = tk.Label(self.canvas, text=self.lang.getText("debit_description"))
        self._tempDebitArrayItems.append(lblDebitDescription)
        lblDebitDescription.place(x=self._w * 0.06, y=self._h * 0.54)
        txtDebitDescription = tk.Text(self.canvas, width=73, height=3, wrap="word")
        self._tempDebitArrayItems.append(txtDebitDescription)
        txtDebitDescription.place(x=self._w * 0.06, y=self._h * 0.59)

        btnSave = tk.Button(self.canvas, text=self.lang.getText("text_button_save"), command=lambda: self.saveDebit(txtAmounth, txtDebitInterest, txtDeadLine, txtDebitDescription))
        self._tempCurrentElementsOptions.append(btnSave)
        self._tempDebitArrayItems.append(btnSave)
        btnSave.place(x=self._w * 0.44, y=self._h * 0.69)

    def drawDebitPayments(self):
        self.deleteDisplayedDrawOption()

        lblSelectYYY = tk.Label(self.canvas, text=self.lang.getText("debit_payments_select_yyyy"))
        self._tempDebitArrayItems.append(lblSelectYYY)
        lblSelectYYY.place(x=self._w * 0.25, y=self._h * 0.4)
        cmbxDebitYYYY = ttk.Combobox(self.canvas, state='readonly', width=6)
        self._tempDebitArrayItems.append(cmbxDebitYYYY)
        cmbxDebitYYYY['values'] = ["2025"] # WIP >> NEED USE CASE TO GET USE DEBIT YEARS
        cmbxDebitYYYY.current(0)
        cmbxDebitYYYY.place(x=self._w * 0.49, y=self._h * 0.4)
        btnViewDebitsByYYYY = tk.Button(self.canvas, text=self.lang.getText("text_button_load"), command=lambda: self._drawDebitPaymentsHistoryOfDebits(cmbxDebitYYYY))
        self._tempDebitArrayItems.append(btnViewDebitsByYYYY)
        btnViewDebitsByYYYY.place(x=self._w * 0.6, y=self._h * 0.395)

    def _drawDebitPaymentsHistoryOfDebits(self, cmbxDebitYYYY):
        _YYYY = cmbxDebitYYYY.get()

        if not _YYYY:
            return
        
        _path = self.manager.controller.pathController.getPathByCODE("ECONOMY_DEBIT")
        _debitData = self.manager.controller.dependencies["debit_use_case_load_all_debits_peer_year"].execute(_path, _YYYY)

        if not _debitData["success"]:
            return
        
        _counter = 1
        H = self._h * 0.47
        X = self._w * 0.2
        dh = (H / 7) * 0.8
        dx = X / 4

        lblBannerConter = tk.Label(self.canvas, text=self.lang.getText("text_number"))
        self._tempDebitArrayItems.append(lblBannerConter)
        lblBannerConter.place(x=self._w * 0.12, y=H)

        lblBannerAmounth = tk.Label(self.canvas, text=self.lang.getText("text_amount"))
        self._tempDebitArrayItems.append(lblBannerAmounth)
        lblBannerAmounth.place(x=self._w * 0.17, y=H)

        lblBannerInterest = tk.Label(self.canvas, text=self.lang.getText("text_interest"))
        self._tempDebitArrayItems.append(lblBannerInterest)
        lblBannerInterest.place(x=self._w * 0.27, y=H)

        lblDeathLine = tk.Label(self.canvas, text=self.lang.getText("text_date_limit"))
        self._tempDebitArrayItems.append(lblDeathLine)
        lblDeathLine.place(x=self._w * 0.38, y=H)

        lblState = tk.Label(self.canvas, text=self.lang.getText("text_status"))
        self._tempDebitArrayItems.append(lblState)
        lblState.place(x=self._w * 0.53, y=H)

        lblActions = tk.Label(self.canvas, text=self.lang.getText("text_actions"))
        self._tempDebitArrayItems.append(lblActions)
        lblActions.place(x=self._w * 0.69, y=H)

        _debit_actions = self.lang.getText("debit_actions")

        for i in _debitData["data"]:
            _data = str(_debitData["data"][i]).split("\n")[0]
            itterData = str(_data).split("|")
            UUID = itterData[0]
            _amounth = itterData[1]
            _interest = itterData[2]
            _deathline = itterData[3]
            _status = itterData[5]

            # ONLY RENDER PENDING DEBITS
            if _status != self.lang.getText("debit_states")[0]:
                continue

            lblCounterDebit = tk.Label(self.canvas, text=str(_counter))
            self._tempDebitArrayItems.append(lblCounterDebit)
            lblCounterDebit.place(x=self._w * 0.12, y= H + (_counter * dh))

            lblAmounthDebit = tk.Label(self.canvas, text=f"${_amounth}")
            self._tempDebitArrayItems.append(lblAmounthDebit)
            lblAmounthDebit.place(x=self._w * 0.17, y= H + (_counter * dh))

            lblInterestdebit = tk.Label(self.canvas, text=f"{_interest} %")
            self._tempDebitArrayItems.append(lblInterestdebit)
            lblInterestdebit.place(x=self._w * 0.27, y= H + (_counter * dh))

            lblDeathLine = tk.Label(self.canvas, text=_deathline)
            self._tempDebitArrayItems.append(lblDeathLine)
            lblDeathLine.place(x=self._w * 0.38, y= H + (_counter * dh))

            lblStatus = tk.Label(self.canvas, text=_status)
            self._tempDebitArrayItems.append(lblStatus)
            lblStatus.place(x=self._w * 0.53, y= H + (_counter * dh))
            
            # WIP: DEBIT ACTIONS
            _counterDX = 0
            for a in _debit_actions:
                _itterDataButtons = str(a).split(":")
                _action_code = _itterDataButtons[0]
                _ico = _itterDataButtons[1]
                btnAction = tk.Button(self.canvas, text=_ico, command=lambda action=_action_code, UUID=UUID: self.on_debit_action(_debitData["data"], action, UUID))
                self._tempDebitArrayItems.append(btnAction)
                btnAction.place(x=self._w * 0.69 + (dx * _counterDX), y= H + (_counter * dh) - 2)
                _counterDX = _counterDX + 1

            _counter = _counter + 1

    def drawDebitHistory(self):
        self.deleteDisplayedDrawOption()

    def deleteDisplayedDrawOption(self):
        for widget in self._tempDebitArrayItems:
            widget.destroy()
        self._tempDebitArrayItems.clear()

    def saveDebit(self, txtAmounth, txtDebitInterest, txtDeadLine, txtDebitDescription):
        _amounth = txtAmounth.get()
        _debitInterest = txtDebitInterest.get()
        _deadLine = txtDeadLine.get()
        _description = txtDebitDescription.get("1.0", tk.END)

        if self.validateDebitFields(_amounth, _debitInterest, _deadLine, _description):
            _path = self.manager.controller.pathController.getPathByCODE("ECONOMY_DEBIT_CURRENT_YYYY")
            _timeStamp = str(self.manager.controller.utils["time_util"].getTimeStamp())
            _currentTime = str(self.manager.controller.utils["time_util"].getCurrentHHMMSS()).replace(":", " ")
            _path = F"{_path}{_timeStamp} {_currentTime}.csv"

            _description = str(_description).replace("\n", " ")
            _debit_states = self.lang.getText("debit_states")
            data = f"{_amounth}|{_debitInterest}|{_deadLine}|{_description}|{_debit_states[0]}"

            _status = self.manager.controller.dependencies["debit_use_case_save_report"].execute(_path, data)

            if _status:
                PopupView(self.master, self.manager, self.lang.getText("ok_economy_save_report"), "SAVE").render(500, 300)
                _path = self.manager.controller.pathController.getPathByCODE("USAGES")
                _path = f"{_path}\\{self.manager.controller.utils["time_util"].getCurrentYYYY()}-debit.txt"
                _data = f"{self.manager.controller.utils["time_util"].getTimeStamp()} {self.manager.controller.utils["time_util"].getCurrentHHMMSS()}"
                self.usageService.save_usage(_path, _data)
            else:
                PopupView(self.master, self.manager, self.lang.getText("error_debit_save_app"), "ERROR").render(500, 300)
        else:
            PopupView(self.master, self.manager, self.lang.getText("error_debit_save"), "ERROR").render(500, 300)

    def on_debit_action(self, debit_data, action, UUID):
        _debit_actions = self.lang.getText("debit_actions")
        _debit_actions = [str(x).split(":")[0] for x in _debit_actions]

        if action == _debit_actions[0]:
            self.viewDebit(debit_data, UUID)
        elif action == _debit_actions[1]:
            self.paymentDebit(debit_data, UUID)
        elif action == _debit_actions[2]:
            self.payDebit(debit_data, UUID)
    def viewDebit(self, debit_data, UUID):
        filename, value = (lambda data, uuid: next(((k, v) for k, v in data.items() if v.startswith(uuid)), (None, None)))(debit_data, UUID)
        
        if filename and value:
            _template = self.lang.getText("debit_view_template")
            _data = str(value).split("|")
            _UUID = _data[0]
            _debit_value = _data[1]
            _debit_interest = _data[2]

            _debit_total = _debit_value
            if float(_debit_interest) > 0:
                _debit_total = float(_debit_total) * (1 + (float(_debit_interest)/100))
                _debit_total = round(_debit_total, 2)
                _debit_total = str(_debit_total)

            _debit_deadline = _data[3]
            _debit_description = _data[4]
            _debit_status = _data[5]

            _template = str(_template).replace("<UUID>", _UUID)
            _template = str(_template).replace("<DEBIT-TOTAL>", _debit_total)
            _template = str(_template).replace("<DEBIT-AMOUNT>", _debit_value)
            _template = str(_template).replace("<DEBIT-DESCRIPTION>", _debit_description)
            _template = str(_template).replace("<DEBIT-INTEREST>", _debit_interest)
            _template = str(_template).replace("<DEBIT-LIMIT>", _debit_deadline)

            PopupView(self.master, self.manager, _template, f"DEBIT: {_debit_status}").render(500, 300)

    def paymentDebit(self, debit_data, UUID):
        print("payment")
        print(UUID)

    def payDebit(self, debit_data, UUID):
        filename, value = (lambda data, uuid: next(((k, v) for k, v in data.items() if v.startswith(uuid)), (None, None)))(debit_data, UUID)

        if filename and value:
            _template = self.lang.getText("debit_pay_template")
            _data = str(value).split("|")
            _UUID = _data[0]
            _debit_value = _data[1]
            _debit_status = _data[5]

            _template = str(_template).replace("<UUID>", _UUID)
            _template = str(_template).replace("<DEBIT-TOTAL>", _debit_value)

            confirm_view = PopupConfirmView(self.master, self.manager, _template, f"DEBIT: {_debit_status}")
            user_choice = confirm_view.render(400, 200)

            if user_choice:
                _YYYY = str(filename).split(" ")[0]
                _path = self.manager.controller.pathController.getPathByCodeAndYYYY("ECONOMY_DEBIT", _YYYY)
                _path = f"{_path}{filename}"
                _YYYYMMDD = self.manager.controller.utils["time_util"].getTimeStamp()
                _YYYYMMDD = str(_YYYYMMDD).replace(" ", "/")
                _statusComment = self.lang.getText("debit_comment_pay")
                _payState = self.lang.getText("debit_states")[1]
                _status = self.manager.controller.dependencies["debit_use_case_pay_debit"].execute(_path, value, _YYYYMMDD, _statusComment, _payState)

                if _status:
                    PopupView(self.master, self.manager, self.lang.getText("ok_economy_save_report"), "UPDATE").render(500, 300)
                    _path = self.manager.controller.pathController.getPathByCODE("USAGES")
                    _path = f"{_path}\\{self.manager.controller.utils["time_util"].getCurrentYYYY()}-debit.txt"
                    _data = f"{self.manager.controller.utils["time_util"].getTimeStamp()} {self.manager.controller.utils["time_util"].getCurrentHHMMSS()}"
                    self.usageService.save_usage(_path, _data)
                else:
                    PopupView(self.master, self.manager, self.lang.getText("error_debit_save_app"), "ERROR").render(500, 300)
            else:
                PopupView(self.master, self.manager, self.lang.getText("text_user_cancelled"), "Cancel").render(500, 300)

    def validateDebitFields(self, txtAmounth, txtDebitInterest, txtDeadLine, txtDebitDescription):
        try:
            if int(txtAmounth) <= 0:
                return False
            
            if float(txtDebitInterest) < 0 or float(txtDebitInterest) > 100:
                return False
            
            if not self.stringProcesor.validateTXT(txtDebitDescription):
                return False
            
            if not self.stringProcesor.validateTXT(txtDeadLine):
                return False

            return True
        except:
            return False
        
    # DEBITS
