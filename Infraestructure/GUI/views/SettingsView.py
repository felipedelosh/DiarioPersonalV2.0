"""
FelipedelosH
2025
"""
import tkinter as tk
from Domain.Enums.PathEnums import PathEnums
from Infraestructure.GUI.Screen import Screen
from Infraestructure.GUI.views.PopupView import PopupView

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
        self.btnMainMenu = None
        _options = self.lang.getText("settings_options")
        self.renderButons(_options, self._w, self._h)

    def renderButons(self, _options, _w, _h):
        self.btnMainMenu = tk.Button(self.canvas, text=self.lang.getText("text_main_menu"), command=self.showMainMenuFromBtn)
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
            self.destroyOption()
            self.drawBtnBackToMainMenu()
            self.drawFilesSettings()


    def drawBtnBackToMainMenu(self):
        self.btnMainMenu.place(x=self._w*0.4, y=self._h*0.1)

    def showMainMenuFromBtn(self):
        self.btnMainMenu.destroy()
        self.destroyOption()
        _options = self.lang.getText("settings_options")
        self.renderButons(_options, self._w, self._h)

    # FILES - BACKUP
    def drawFilesSettings(self):
        lblHelp = tk.Label(self.canvas, text=self.lang.getText("settings_option_files_help_generate_backup_file"))
        self._tempCurrentElementsOptions.append(lblHelp)
        lblHelp.place(x=self._w * 0.3, y=self._h * 0.3)

        btnCreateBackupAllTemp = tk.Button(self.canvas, text=self.lang.getText("text_button_save"), command=self.generateBackupTempFile)
        self._tempCurrentElementsOptions.append(btnCreateBackupAllTemp)
        btnCreateBackupAllTemp.place(x=self._w * 0.45, y=self._h * 0.4)

    def generateBackupTempFile(self):
        _path_dic = self.manager.controller.pathController.getAllBasePathInDict()
        _path_temp_file = self.manager.controller.pathController.getPathByCODE(str(PathEnums.TEMP))
        _path_temp_file = f"{_path_temp_file}all.txt"
        backup_file_header_template = self.lang.getText("settings_option_files_header_backup_file_template")
        _status = self.manager.controller.dependencies["diary_use_case_get_all_registred_information_with_temp_file"].execute(_path_dic, _path_temp_file, backup_file_header_template)
        
        if _status["success"]:
            PopupView(self.master, self.manager, self.lang.getText("text_ok_to_save"), "SAVE").render(500, 300)
    # FILES - BACKUP

    def destroyOption(self):
        for widget in self._tempCurrentElementsOptions:
            widget.destroy()
        self._tempCurrentElementsOptions.clear()

        for btn in self.btns:
            btn.destroy()
        self.btns.clear()
