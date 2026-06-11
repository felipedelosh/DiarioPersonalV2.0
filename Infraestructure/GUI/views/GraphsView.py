"""
FelipedelosH
2025
"""
import tkinter as tk
from tkinter import ttk as ttk
from Infraestructure.GUI.Screen import Screen
from Infraestructure.GUI.views.PopupView import PopupView
from Infraestructure.GUI.views.PopupDateInputView import PopupDateInputView
from Domain.Enums.GraphicsEnums import GraphType
from Domain.Enums.GraphicsEnums import GraphEconomyFilters


class GraphsView(Screen):
    def render(self, x, y):
        self.canvas["bg"]="snow"
        self.canvas.place(x=x, y=y)
        self._w = float(self.canvas["width"])
        self._h = float(self.canvas["height"])
        self.lang = self.manager.controller.dependencies["lang"]
        # PAINTED CANVAS
        self.auxiliarCanvas = tk.Canvas(self.canvas, bg="snow", highlightthickness=1, highlightbackground="black")
        self.auxiliarCanvas["width"] = self._w * 0.9
        self.auxiliarCanvas["height"] = self._h * 0.55
        # END PAINTED CANVAS
        self._tempCurrentElementsOptions = [] # TO DELETE AFTER USE OR CHANGE VIEW
        self.btns = []
        _options = self.lang.getText("graphics_options")
        lblTitle = tk.Label(self.canvas, text=self.lang.getText("graphics_title_message"))
        lblTitle.place(x=self._w*0.4, y=self._h*0.05)
        # VARS
        self.txtDateInit = None
        self.txtDateEnd = None
        self._tempFilterElementsOptions = {}
        # VARS
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
        lblHelpFilterByEconomyGraphics = tk.Label(self.canvas, text=self.lang.getText("text_graphic_type"))
        self._tempCurrentElementsOptions.append(lblHelpFilterByEconomyGraphics)
        lblHelpFilterByEconomyGraphics.place(x=self._w * 0.05, y=self._h * 0.2)
        cmbxEconomyOptionsGraphicsTypes = ttk.Combobox(self.canvas, state='readonly', width=13)
        cmbxEconomyOptionsGraphicsTypes["values"] = self.lang.getText("graphics_economy_categories")
        cmbxEconomyOptionsGraphicsTypes.current(0)
        self._tempCurrentElementsOptions.append(cmbxEconomyOptionsGraphicsTypes)
        cmbxEconomyOptionsGraphicsTypes.place(x=self._w * 0.2, y=self._h * 0.2)
        lblHelpTypeOfFilter = tk.Label(self.canvas, text=self.lang.getText("text_graphic_type_of_filter"))
        self._tempCurrentElementsOptions.append(lblHelpTypeOfFilter)
        lblHelpTypeOfFilter.place(x=self._w * 0.45, y=self._h * 0.2)
        cmbxEconomyOptionsGraphicsFilters = ttk.Combobox(self.canvas, state='readonly', width=36)
        cmbxEconomyOptionsGraphicsFilters.bind("<<ComboboxSelected>>", self.onEconomyFilterChanged)
        cmbxEconomyOptionsGraphicsFilters["values"] = self.lang.getText("graphics_economy_categories_filters")
        cmbxEconomyOptionsGraphicsFilters.current(0)
        self._tempCurrentElementsOptions.append(cmbxEconomyOptionsGraphicsFilters)
        cmbxEconomyOptionsGraphicsFilters.place(x=self._w * 0.58, y=self._h * 0.2)

        btnPaint = tk.Button(self.canvas, bg="green", text=self.lang.getText("text_button_graphic"), command=lambda: self.paintEconomy(cmbxEconomyOptionsGraphicsTypes.get(), cmbxEconomyOptionsGraphicsFilters.get()))
        self._tempCurrentElementsOptions.append(btnPaint)
        btnPaint.place(x=self._w * 0.45, y=self._h * 0.34)

    # Draw Filter Elements
    def onEconomyFilterChanged(self, event):
        self.deleteFilterOptions()
        combo = event.widget
        selected_value = combo.get()

        # No filter
        if selected_value == self.lang.getText("graphics_economy_categories_filters")[0]:
            print("mostrar todo")

        # Date
        elif selected_value == self.lang.getText("graphics_economy_categories_filters")[1]:
            self._tempFilterElementsOptions[selected_value] = []
            lblHelpDateInit = tk.Label(self.canvas, text=self.lang.getText("text_init_date"))
            self._tempCurrentElementsOptions.append(lblHelpDateInit)
            self._tempFilterElementsOptions[selected_value].append(lblHelpDateInit)
            lblHelpDateInit.place(x=self._w * 0.1, y=self._h * 0.26)
            self.txtDateInit = tk.Entry(self.canvas, width=14, fg="gray")
            self.txtDateInit.insert(0, self.lang.getText("text_format_date"))
            self.txtDateInit.bind("<FocusIn>", lambda event, txt=self.txtDateInit: self._open_date_popup(txt))
            self._tempCurrentElementsOptions.append(self.txtDateInit)
            self._tempFilterElementsOptions[selected_value].append(self.txtDateInit)
            self.txtDateInit.place(x=self._w*0.22, y=self._h*0.26)
            lblHelpDateEnd = tk.Label(self.canvas, text=self.lang.getText("text_final_date"))
            self._tempCurrentElementsOptions.append(lblHelpDateEnd)
            self._tempFilterElementsOptions[selected_value].append(lblHelpDateEnd)
            lblHelpDateEnd.place(x=self._w * 0.5, y=self._h * 0.26)
            self.txtDateEnd = tk.Entry(self.canvas, width=14, fg="gray")
            self.txtDateEnd.insert(0, self.lang.getText("text_format_date"))
            self.txtDateEnd.bind("<FocusIn>", lambda event, txt=self.txtDateEnd: self._open_date_popup(txt))
            self._tempCurrentElementsOptions.append(self.txtDateEnd)
            self._tempFilterElementsOptions[selected_value].append(self.txtDateEnd)
            self.txtDateEnd.place(x=self._w * 0.61, y=self._h * 0.26)

        # Dreams VS Sleep
        elif selected_value == self.lang.getText("graphics_economy_categories_filters")[2]:
            print("ZZZ vs $$$")

        # Categories
        elif selected_value == self.lang.getText("graphics_economy_categories_filters")[3]:
            print("filtrado por categorias")

        else:
            return
        
    def _open_date_popup(self, entry):
        current_value = entry.get().strip()

        if current_value == "" or current_value == self.lang.getText("text_format_date"):
            popup = PopupDateInputView(self.master, self.manager.controller.utils["time_util"], self.manager, self.lang.getText("text_insert_date"), self.lang.getText("text_date"))

            selected_date = popup.render(420, 220)
            if selected_date is not None and str(selected_date).strip() != "":
                entry.delete(0, tk.END)
                entry.insert(0, selected_date)
                entry.config(fg="black")
            else:
                self._add_placeholder_date(entry)
                self.master.focus_set()

    def _add_placeholder_date(self, entry):
        if not entry.get():
            entry.insert(0, self.lang.getText("text_format_date"))
            entry.config(fg="gray")

    def _clear_placeholder_date(self, entry):
        if entry.get() == self.lang.getText("text_format_date"):
            entry.delete(0, tk.END)
            entry.config(fg="black")

    def paintEconomy(self, option, filter):
        # Type of Graph
        # PIE
        if option == self.lang.getText("graphics_economy_categories")[0]:
            self.paintedCanvas(GraphType.PIE, filter)
        # BAR
        if option == self.lang.getText("graphics_economy_categories")[1]:
            self.paintedCanvas(GraphType.BAR, filter)
        # LINE
        if option == self.lang.getText("graphics_economy_categories")[2]:
            self.paintedCanvas(GraphType.LINE, filter)
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

    def paintedCanvas(self, graphicsType: GraphType, filter: str):
        _data = None

        if graphicsType == GraphType.PIE:
            _base_path = self.manager.controller.pathController.getPathByCODE("ECONOMY_TACCOUNTS")
            _data = self.manager.controller.dependencies["economy_use_case_get_all_taccounts"].execute(_base_path)
            _data = self.applyFilterToData(filter, _data)

            if not _data["success"]:
                PopupView(self.master, self.manager, self.lang.getText("text_find_error_taccounts_search"), "ERROR").render(500, 300)
                return None
        elif graphicsType == GraphType.BAR:
            _base_path = self.manager.controller.pathController.getPathByCODE("ECONOMY_TACCOUNTS")
            _data = self.manager.controller.dependencies["economy_use_case_get_all_taccounts"].execute(_base_path)
            _data = self.applyFilterToData(filter, _data)

            if not _data["success"]:
                PopupView(self.master, self.manager, self.lang.getText("text_find_error_taccounts_search"), "ERROR").render(500, 300)
                return None
        elif graphicsType == GraphType.LINE:
            _base_path = self.manager.controller.pathController.getPathByCODE("ECONOMY_TACCOUNTS")
            _data = self.manager.controller.dependencies["economy_use_case_get_all_taccounts_segmented_by_year"].execute(_base_path)
            _data = self.applyFilterToData(filter, _data)

            if not _data["success"]:
                PopupView(self.master, self.manager, self.lang.getText("text_find_error_taccounts_search"), "ERROR").render(500, 300)
                return None
        else:
            return None
        
        self.auxiliarCanvas.delete("all")
        graphier = self.manager.controller.utils["graphics_renderder"]
        _MMNames = self.lang.getText("month_names")
        self.auxiliarCanvas.place(x=self._w * 0.05, y=self._h * 0.40)

        options = {
            'MMNames' : _MMNames
        }

        graphier.render(self.auxiliarCanvas, _data, graphicsType, options)

    def applyFilterToData(self, filter, data):
        _data = data
        # No filter
        if filter == self.lang.getText("graphics_economy_categories_filters")[0]:
            return _data

        # Date
        if filter == self.lang.getText("graphics_economy_categories_filters")[1]:
            _dateA = self.txtDateInit.get()
            _dateB = self.txtDateEnd.get()
            print("filtrar por fecha")
            print(_dateA)
            print(_dateB)

        # Dreams VS Sleep
        if filter == self.lang.getText("graphics_economy_categories_filters")[2]:
            print("ZZZ vs $$$")

        # Categories
        if filter == self.lang.getText("graphics_economy_categories_filters")[3]:
            print("Filtrar por categorias")

        return _data

    def deleteOption(self):
        for widget in self._tempCurrentElementsOptions:
            widget.destroy()
        self._tempCurrentElementsOptions.clear()

        if hasattr(self, "auxiliarCanvas") and self.auxiliarCanvas:
            self.auxiliarCanvas.delete("all")
            self.auxiliarCanvas.place_forget()

    def deleteFilterOptions(self):
        for widgets in self._tempFilterElementsOptions.values():
            for widget in widgets:
                widget.destroy()

        self._tempFilterElementsOptions.clear()
        self.txtDateInit = None
        self.txtDateEnd = None
