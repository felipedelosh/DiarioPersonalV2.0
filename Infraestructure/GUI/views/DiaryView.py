"""
FelipedelosH
2025
"""
import tkinter as tk
import random
from tkinter import ttk as ttk
from Infraestructure.GUI.Screen import Screen
from Infraestructure.GUI.views.PopupView import PopupView

class DiaryView(Screen):
    def render(self, x, y):
        self.canvas["bg"]="purple"
        self.canvas.place(x=x, y=y)
        self._w = float(self.canvas["width"])
        self._h =float(self.canvas["height"])
        self.is_secret = False
        self.lang = self.manager.controller.dependencies["lang"]
        self.stringProcesor = self.manager.controller.utils["string_procesor"]
        self.usageService = self.manager.controller.dependencies["usage_service"]
        self.btns = []
        self._tempCurrentElementsOptions = [] # TO DELETE AFTER USE OR CHANGE VIEW
        _options = self.lang.getText("diary_options")
        lblTitle = tk.Label(self.canvas, text=self.lang.getText("diary_title_message"))
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
                btn.place(x=current_x, y=_h * 0.18)
                current_x += btn.winfo_reqwidth() + _spacing

    def drawBtnInterface(self, _options, opt):
        if opt == _options[0]:
            self.deleteOption()
            self.drawDiaryOption()
        if opt == _options[1]:
            self.deleteOption()
            self.drawDreamsOption()
        if opt == _options[2]:
            self.deleteOption()
            print("Amigos")
        if opt == _options[3]:
            self.deleteOption()
            print("Notas")
        if opt == _options[4]:
            self.deleteOption()
            self.drawFeelOption()
        if opt == _options[5]:
            self.deleteOption()
            self.drawDrugsOption()

    # DIARY
    def drawDiaryOption(self):
        txtEntryTitle = tk.Entry(self.canvas, fg="gray")
        self._tempCurrentElementsOptions.append(txtEntryTitle)
        txtEntryTitle.insert(0, self.lang.getText("diary_page_insert_title"))
        txtEntryTitle.bind("<FocusIn>", lambda e, entry=txtEntryTitle: self._clear_placeholder_diary_page_title(entry))
        txtEntryTitle.bind("<FocusOut>", lambda e, entry=txtEntryTitle: self._add_placeholder_diary_page_title(entry))
        txtEntryTitle.place(x=self._w*0.07, y=self._h*0.3, width=self._w*0.5, height=25)
        txtText = tk.Text(self.canvas, height = 20, width = 70, wrap="word")
        self._tempCurrentElementsOptions.append(txtText)
        txtText.place(x=self._w*0.07, y=self._h*0.38)
        btnSecret = tk.Button(self.canvas, text="🔓")
        btnSecret.config(command=lambda b=btnSecret: self.toggleScret(b))
        self._tempCurrentElementsOptions.append(btnSecret)
        btnSecret.place(x=self._w*0.6, y=self._h*0.3)
        btnSave = tk.Button(self.canvas, text=self.lang.getText("text_button_save"), command=lambda: self.savePageDiary(txtEntryTitle, txtText))
        self._tempCurrentElementsOptions.append(btnSave)
        btnSave.place(x=self._w*0.65, y=self._h*0.3)
        btnLoad = tk.Button(self.canvas, text=self.lang.getText("text_button_load"), command=lambda: self.loadPageDiary(txtEntryTitle, txtText))
        self._tempCurrentElementsOptions.append(btnLoad)
        btnLoad.place(x=self._w*0.75, y=self._h*0.3)
        btnSearch = tk.Button(self.canvas, text=self.lang.getText("text_button_search"))
        self._tempCurrentElementsOptions.append(btnSearch)
        btnSearch.place(x=self._w*0.85, y=self._h*0.3)

    def _clear_placeholder_diary_page_title(self, entry):
        if entry.get() == self.lang.getText("diary_page_insert_title"):
            entry.delete(0, tk.END)
            entry.config(fg="black")
    def _add_placeholder_diary_page_title(self, entry):
        if not entry.get():
            entry.insert(0, self.lang.getText("diary_page_insert_title"))
            entry.config(fg="gray")

    def toggleScret(self, btnSecret):
        self.is_secret = not self.is_secret

        if self.is_secret:
            btnSecret["text"] = "🔒"
        else:
            btnSecret["text"] = "🔓"

    def deleteOption(self):
        for widget in self._tempCurrentElementsOptions:
            widget.destroy()
        self._tempCurrentElementsOptions.clear()

    #METHODS
    def savePageDiary(self, txtEntryTitle, txtText):
        title = txtEntryTitle.get()
        text = txtText.get("1.0", tk.END)
        
        if title == self.lang.getText("diary_page_insert_title"):
            PopupView(self.master, self.manager, self.lang.getText("error_diary_page_insert_title"), "ERROR").render(500, 300)
            return

        if not self.stringProcesor.validateTXT(title):
            PopupView(self.master, self.manager, self.lang.getText("error_diary_page_insert_title"), "ERROR").render(500, 300)
            return

        if not self.stringProcesor.validateTXT(text):
            PopupView(self.master, self.manager, self.lang.getText("error_diary_page_insert_title"), "ERROR").render(500, 300)
            return

        _path = self.manager.controller.pathController.getPathByCODE("DIARY_CURRENT_YYYY")
        _path = _path + f"{self.manager.controller.utils["time_util"].getTimeStamp()} - {title}.txt"
        text = text + "\n\n" + self.manager.controller.utils["time_util"].getTimeSignature() + "\n\n"
        if self.is_secret:
            _path = _path.rsplit(".txt", 1)[0] + ".secret.txt"
            _excrypted = self.manager.controller.utils["enigma"].processEncryptText(text)
            text = _excrypted
        _status = self.manager.controller.dependencies["diary_use_case_save_page"].execute(_path, text)

        if _status:
            PopupView(self.master, self.manager, self.lang.getText("ok_diary_page_save"), "SAVE").render(500, 300)
            _path = self.manager.controller.pathController.getPathByCODE("USAGES")
            _path = f"{_path}\\{self.manager.controller.utils["time_util"].getCurrentYYYY()}-diary.txt"
            _data = f"{self.manager.controller.utils["time_util"].getTimeStamp()} {self.manager.controller.utils["time_util"].getCurrentHHMMSS()}"
            self.usageService.save_usage(_path, _data)
            self._clearEntrysPageDiary(txtEntryTitle, txtText)
        else:
            PopupView(self.master, self.manager, self.lang.getText("error_diary_page_save"), "ERROR").render(500, 300)
            return

    def loadPageDiary(self, txtEntryTitle, txtText):
        title = txtEntryTitle.get()
        
        if title == self.lang.getText("diary_page_insert_title"):
            PopupView(self.master, self.manager, self.lang.getText("error_diary_page_insert_title"), "ERROR").render(500, 300)
            return
        
        if not self.stringProcesor.validateTXT(title):
            PopupView(self.master, self.manager, self.lang.getText("error_diary_page_insert_title"), "ERROR").render(500, 300)
            return
        
        _path = self.manager.controller.pathController.getPathByCODE("DIARY_CURRENT_YYYY")
        _data = self.manager.controller.dependencies["diary_use_case_load_page"].execute(_path, title)

        if _data["success"]:
            title = _data["data"]["title"]
            title = str(title).split(" - ", 1)[1]
            content = _data["data"]["content"]
            if ".secret" in title:
                title = title.rsplit(".secret", 1)[0]
                content = self.manager.controller.utils["enigma"].processDecryptText(content)
            title = title.rsplit(".txt", 1)[0]

            self._clearEntrysPageDiary(txtEntryTitle, txtText)
            self._insertTextInEntrys(txtEntryTitle, title, txtText, content)


    def openDiaryPagesReader(self):
        pass

    def _clearEntrysPageDiary(self, txtEntryTitle, txtText):
        txtEntryTitle.delete(0, tk.END)
        txtText.delete("1.0", tk.END)

    def _insertTextInEntrys(self, txtEntryTitle, title, txtText, content):
        txtEntryTitle.insert(tk.END, title)
        txtText.insert("1.0", content)
    # DIARY

    # DREAMS
    def drawDreamsOption(self):
        txtEntryTitle = tk.Entry(self.canvas, fg="gray")
        self._tempCurrentElementsOptions.append(txtEntryTitle)
        txtEntryTitle.insert(0, self.lang.getText("diary_page_insert_title"))
        txtEntryTitle.bind("<FocusIn>", lambda e, entry=txtEntryTitle: self._clear_placeholder_diary_page_title(entry))
        txtEntryTitle.bind("<FocusOut>", lambda e, entry=txtEntryTitle: self._add_placeholder_diary_page_title(entry))
        txtEntryTitle.place(x=self._w*0.07, y=self._h*0.3, width=self._w*0.5, height=25)
        txtText = tk.Text(self.canvas, height = 20, width = 70, wrap="word")
        self._tempCurrentElementsOptions.append(txtText)
        txtText.place(x=self._w*0.07, y=self._h*0.38)
        btnSave = tk.Button(self.canvas, text=self.lang.getText("text_button_save"), command=lambda: self.saveDreamPage(txtEntryTitle, txtText))
        self._tempCurrentElementsOptions.append(btnSave)
        btnSave.place(x=self._w*0.63, y=self._h*0.3)
        btnLoad = tk.Button(self.canvas, text=self.lang.getText("text_button_load"), command=lambda: self.loadDreamPage(txtEntryTitle, txtText))
        self._tempCurrentElementsOptions.append(btnLoad)
        btnLoad.place(x=self._w*0.73, y=self._h*0.3)
        btnSearch = tk.Button(self.canvas, text=self.lang.getText("text_button_search"))
        self._tempCurrentElementsOptions.append(btnSearch)
        btnSearch.place(x=self._w*0.83, y=self._h*0.3)

    def saveDreamPage(self, txtEntryTitle, txtText):
        title = txtEntryTitle.get()
        text = txtText.get("1.0", tk.END)
        
        if title == self.lang.getText("diary_page_insert_title"):
            PopupView(self.master, self.manager, self.lang.getText("error_dream_page_insert_title"), "ERROR").render(500, 300)
            return

        if not self.stringProcesor.validateTXT(title):
            PopupView(self.master, self.manager, self.lang.getText("error_dream_page_insert_title"), "ERROR").render(500, 300)
            return

        if not self.stringProcesor.validateTXT(text):
            PopupView(self.master, self.manager, self.lang.getText("error_dream_page_insert_text"), "ERROR").render(500, 300)
            return
        
        _path = self.manager.controller.pathController.getPathByCODE("DREAM_CURRENT_YYYY")
        _path = _path + f"{self.manager.controller.utils["time_util"].getTimeStamp()} - {title}.txt"
        text = text + "\n\n" + self.manager.controller.utils["time_util"].getTimeSignature() + "\n\n"
        _status = self.manager.controller.dependencies["dream_use_case_save_dream"].execute(_path, text)

        if _status:
            PopupView(self.master, self.manager, self.lang.getText("ok_diary_page_save"), "SAVE").render(500, 300)
            _path = self.manager.controller.pathController.getPathByCODE("USAGES")
            _path = f"{_path}\\{self.manager.controller.utils["time_util"].getCurrentYYYY()}-dreams.txt"
            _data = f"{self.manager.controller.utils["time_util"].getTimeStamp()} {self.manager.controller.utils["time_util"].getCurrentHHMMSS()}"
            self.usageService.save_usage(_path, _data)
            self._clearEntrysPageDiary(txtEntryTitle, txtText)
        else:
            PopupView(self.master, self.manager, self.lang.getText("error_diary_page_save"), "ERROR").render(500, 300)
            return
        
    def loadDreamPage(self, txtEntryTitle, txtText):
        title = txtEntryTitle.get()
        
        if title == self.lang.getText("diary_page_insert_title"):
            PopupView(self.master, self.manager, self.lang.getText("error_dream_page_insert_title"), "ERROR").render(500, 300)
            return
        
        if not self.stringProcesor.validateTXT(title):
            PopupView(self.master, self.manager, self.lang.getText("error_dream_page_insert_title"), "ERROR").render(500, 300)
            return
        
        _path = self.manager.controller.pathController.getPathByCODE("DREAM_CURRENT_YYYY")
        _data = self.manager.controller.dependencies["dream_use_case_load_dream"].execute(_path, title)

        if _data["success"]:
            title = _data["data"]["title"]
            title = str(title).split(" - ", 1)[1]
            content = _data["data"]["content"]
            title = title.rsplit(".txt", 1)[0]

            self._clearEntrysPageDiary(txtEntryTitle, txtText)
            self._insertTextInEntrys(txtEntryTitle, title, txtText, content)
    # DREAMS

    # FEELINGS
    def drawFeelOption(self):
        lblTitleFeelings = tk.Label(self.canvas, text=self.lang.getText("title_feelings"))
        self._tempCurrentElementsOptions.append(lblTitleFeelings)
        lblTitleFeelings.place(x=self._w*0.4, y=self._h*0.3)
        lblHelpFeelings = tk.Label(self.canvas, text=self.lang.getText("help_feelings"))
        self._tempCurrentElementsOptions.append(lblHelpFeelings)
        lblHelpFeelings.place(x=self._w*0.38, y=self._h*0.36)
        cmbxFeelings = ttk.Combobox(self.canvas, state='readonly')
        self._tempCurrentElementsOptions.append(cmbxFeelings)
        cmbxFeelings['values'] = self.lang.getText("list_feelings")
        cmbxFeelings.place(x=self._w*0.418, y=self._h*0.42)
        btnSaveFeeling = tk.Button(self.canvas, text=self.lang.getText("text_button_save"), command=lambda: self.saveFeeling(cmbxFeelings))
        self._tempCurrentElementsOptions.append(btnSaveFeeling)
        btnSaveFeeling.place(x=self._w*0.48, y=self._h*0.5)

    def saveFeeling(self, cmbxFeelings):
        feeling = cmbxFeelings.get()
        if str(feeling).strip() != "":
            _path = self.manager.controller.pathController.getPathByCODE("FEELING_CURRENT_YYYY")
            _path = f"{_path}\\{self.manager.controller.utils["time_util"].getTimeStamp()}.txt"
            _status = self.manager.controller.dependencies["feeling_use_case_save"].execute(_path, feeling)

            if _status:
                PopupView(self.master, self.manager, self.lang.getText("ok_feelings_not_feel"), "OK").render(500, 300)
                _path = self.manager.controller.pathController.getPathByCODE("USAGES")
                _path = f"{_path}\\{self.manager.controller.utils["time_util"].getCurrentYYYY()}-feelings.txt"
                _data = f"{self.manager.controller.utils["time_util"].getTimeStamp()} {self.manager.controller.utils["time_util"].getCurrentHHMMSS()}"
                self.usageService.save_usage(_path, _data)
            else:
                PopupView(self.master, self.manager, self.lang.getText("error_feelings_fatal"), "ERROR FATAL").render(500, 300)
        else:
            PopupView(self.master, self.manager, self.lang.getText("error_feelings_not_feel"), "ERROR").render(500, 300)
            return
    # FEELINGS

    # DRUGS
    def drawDrugsOption(self):
        lblTitleDrugs = tk.Label(self.canvas, text=self.lang.getText("drugs_use_title"))
        self._tempCurrentElementsOptions.append(lblTitleDrugs)
        lblTitleDrugs.place(x=self._w*0.07, y=self._h*0.3)
        _drugs_message = random.choice(self.lang.getText("drugs_use_help_text"))
        lblHelpDrugs = tk.Label(self.canvas, text=_drugs_message)
        self._tempCurrentElementsOptions.append(lblHelpDrugs)
        lblHelpDrugs.place(x=self._w*0.07, y=self._h*0.36)
        lblDrugsUseInsert = tk.Label(self.canvas, text=self.lang.getText("drugs_use_insert"))
        self._tempCurrentElementsOptions.append(lblDrugsUseInsert)
        lblDrugsUseInsert.place(x=self._w*0.07, y=self._h*0.44)
        cmbxDrugs = ttk.Combobox(self.canvas, state='readonly')
        self._tempCurrentElementsOptions.append(cmbxDrugs)
        cmbxDrugs['values'] = self.lang.getText("list_drugs")
        cmbxDrugs.place(x=self._w*0.42, y=self._h*0.44)
        lblDrugsUsetriggerInsert = tk.Label(self.canvas, text=self.lang.getText("drugs_use_trigger_insert"))
        self._tempCurrentElementsOptions.append(lblDrugsUsetriggerInsert)
        lblDrugsUsetriggerInsert.place(x=self._w*0.07, y=self._h*0.5)
        txtDrugsUsetrigger = tk.Text(self.canvas, height = 2, width = 70, wrap="word")
        self._tempCurrentElementsOptions.append(txtDrugsUsetrigger)
        txtDrugsUsetrigger.place(x=self._w*0.07, y=self._h*0.55)
        lblDrugsUseFeel = tk.Label(self.canvas, text=self.lang.getText("drugs_use_feel"))
        self._tempCurrentElementsOptions.append(lblDrugsUseFeel)
        lblDrugsUseFeel.place(x=self._w*0.07, y=self._h*0.65)
        txtDrugsUseFeel = tk.Text(self.canvas, height = 2, width = 70, wrap="word")
        self._tempCurrentElementsOptions.append(txtDrugsUseFeel)
        txtDrugsUseFeel.place(x=self._w*0.07, y=self._h*0.7)
        btnSaveDrug = tk.Button(self.canvas, text=self.lang.getText("text_button_save"), command=lambda: self.saveDrugUse(cmbxDrugs, txtDrugsUsetrigger, txtDrugsUseFeel))
        self._tempCurrentElementsOptions.append(btnSaveDrug)
        btnSaveDrug.place(x=self._w*0.48, y=self._h*0.85)

    def saveDrugUse(self, cmbxDrugs, txtDrugsUsetrigger, txtDrugsUseFeel):
        _drug = cmbxDrugs.get()
        _trigger = txtDrugsUsetrigger.get("1.0", tk.END)
        _feel = txtDrugsUseFeel.get("1.0", tk.END)

        if str(_drug).strip() != "":
            if not self.stringProcesor.validateTXT(_trigger):
                PopupView(self.master, self.manager, self.lang.getText("error_drugs_usage_insert_trigger"), "ERROR").render(500, 300)
                return
            
            if not self.stringProcesor.validateTXT(_feel):
                PopupView(self.master, self.manager, self.lang.getText("error_drugs_usage_insert_feel"), "ERROR").render(500, 300)
                return
            
            content = _trigger + "\n\n\n" + _feel + "\n" + self.manager.controller.utils["time_util"].getCurrentHHMMSS() + "\n"
            _path = self.manager.controller.pathController.getPathByCODE("DRUGS_CURRENT_YYYY")
            _path = f"{_path}\\{_drug} - {self.manager.controller.utils["time_util"].getTimeStamp()}.txt"
            _status = self.manager.controller.dependencies["drug_use_case_save_usage"].execute(_path, content)

            if _status:
                PopupView(self.master, self.manager, self.lang.getText("ok_drug_save"), "OK").render(500, 300)
                _path = self.manager.controller.pathController.getPathByCODE("USAGES")
                _path = f"{_path}\\{self.manager.controller.utils["time_util"].getCurrentYYYY()}-drugs.txt"
                _data = f"{self.manager.controller.utils["time_util"].getTimeStamp()} {self.manager.controller.utils["time_util"].getCurrentHHMMSS()}"
                self.usageService.save_usage(_path, _data)
            else:
                PopupView(self.master, self.manager, self.lang.getText("error_drugs_fatal"), "ERROR FATAL").render(500, 300)
        else:
            PopupView(self.master, self.manager, self.lang.getText("error_drugs_not_drug"), "ERROR").render(500, 300)
            return
    # DRUGS
