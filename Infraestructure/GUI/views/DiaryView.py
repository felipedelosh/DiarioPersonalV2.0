"""
FelipedelosH
2025
"""
import tkinter as tk
from Infraestructure.GUI.Screen import Screen
from Infraestructure.GUI.views.PopupView import PopupView

class DiaryView(Screen):
    def render(self, x, y):
        self.canvas["bg"]="purple"
        self.canvas.place(x=x, y=y)
        self._w = float(self.canvas["width"])
        self._h =float(self.canvas["height"])
        self.lang = self.manager.controller.dependencies["lang"]
        self.stringProcesor = self.manager.controller.utils["string_procesor"]
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
            print("Sueños")
        if opt == _options[2]:
            self.deleteOption()
            print("Amigos")
        if opt == _options[3]:
            self.deleteOption()
            print("Notas")
        if opt == _options[4]:
            self.deleteOption()
            print("Registro de Sentimientos")
        if opt == _options[5]:
            self.deleteOption()
            print("Drogas")

    def drawDiaryOption(self):
        txtEntryTitle = tk.Entry(self.canvas, fg="gray")
        self._tempCurrentElementsOptions.append(txtEntryTitle)
        txtEntryTitle.insert(0, self.lang.getText("diary_page_insert_title"))
        txtEntryTitle.bind("<FocusIn>", lambda e, entry=txtEntryTitle: self._clear_placeholder_diary_page_title(entry))
        txtEntryTitle.bind("<FocusOut>", lambda e, entry=txtEntryTitle: self._add_placeholder_diary_page_title(entry))
        txtEntryTitle.place(x=self._w*0.07, y=self._h*0.3, width=self._w*0.5, height=25)
        txtText = tk.Text(self.canvas, height = 20, width = 70)
        self._tempCurrentElementsOptions.append(txtText)
        txtText.place(x=self._w*0.07, y=self._h*0.38)
        btnSave = tk.Button(self.canvas, text=self.lang.getText("text_button_save"), command=lambda: self.savePageDiary(txtEntryTitle, txtText))
        self._tempCurrentElementsOptions.append(btnSave)
        btnSave.place(x=self._w*0.6, y=self._h*0.3)
        btnLoad = tk.Button(self.canvas, text=self.lang.getText("text_button_load"))
        self._tempCurrentElementsOptions.append(btnLoad)
        btnLoad.place(x=self._w*0.7, y=self._h*0.3)
        btnSearch = tk.Button(self.canvas, text=self.lang.getText("text_button_search"))
        self._tempCurrentElementsOptions.append(btnSearch)
        btnSearch.place(x=self._w*0.8, y=self._h*0.3)

    def _clear_placeholder_diary_page_title(self, entry):
        if entry.get() == self.lang.getText("diary_page_insert_title"):
            entry.delete(0, tk.END)
            entry.config(fg="black")
    def _add_placeholder_diary_page_title(self, entry):
        if not entry.get():
            entry.insert(0, self.lang.getText("diary_page_insert_title"))
            entry.config(fg="gray")

    def deleteOption(self):
        for widget in self._tempCurrentElementsOptions:
            widget.destroy()
        self._tempCurrentElementsOptions.clear()

    #METHODS
    def savePageDiary(self, txtEntryTitle, txtText):
        title = txtEntryTitle.get()
        text = txtText.get("1.0", tk.END)
        
        if title == self.lang.getText("diary_page_insert_title"):
            popup = PopupView(self.master, self.manager, self.lang.getText("error_diary_page_insert_title"))
            popup.render()

        if not self.stringProcesor.validateTXT(title):
            popup = PopupView(self.master, self.manager, self.lang.getText("error_diary_page_insert_title"))
            popup.render()

    def loadPageDiary(self):
        pass

    def openDiaryPagesReader(self):
        pass
