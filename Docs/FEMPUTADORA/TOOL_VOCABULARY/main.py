"""
FelipedelosH
2026

Generates a VOCABULARY FILE to FEMPUTADORA
KEY = [#, ...#]
"""
from tkinter import *
from tkinter import ttk
from controller import *

class Software:
    def __init__(self) -> None:
        self._w = 900
        self._h = 600
        self.controller = Controller()
        self.screem = Tk()
        self.canvas = Canvas(self.screem)
        self.lblBannerProgram = Label(self.canvas, text="Generates a file to FEMPUTADORA VOCABULARY...")
        self.lblFooterProgram = Label(self.canvas, text="FelipedelosH")

        self.lblVocabularyVr = Label(self.canvas, text="Versión: ")
        self.cmbxVocabularyFiles = ttk.Combobox(self.canvas)
        self.cmbxVocabularyFiles["values"] = ["NEW"]

        self.lblSemanticFieldsTitle = Label(self.canvas, text="Dimensión semantica:")
        self.btnAddSemanticDimension = Button(self.canvas, bg="green", text="ADD new D", command=self.showDimensionSemanticInFooter)

        self.lblTitleSemanticDimension = Label(self.canvas, text="Nombre de dimesión semantica: ")
        self.txtTitleSemanticDimension = Entry(self.canvas, width=30)
        self.lblTitleIteratorsContextual = Label(self.canvas, text="Ingrese los iteradores contextuales: ")
        self.txtTitleIteratorsContextual = Entry(self.canvas, width=80)
        self.lblSemanticDimensionDescription = Label(self.canvas, text="Ingresa la descripción:")
        self.txtSemanticDimensionDescription = Entry(self.canvas, width=80)

        self.btnSaveSemanticDimension = Button(self.canvas, text="GUARDAR", command=self.setSemanticDimsension)


        # VARS
        self._tempSemanticDimensionsOptions = []

        self.vizualizedAndRun()


    def vizualizedAndRun(self):
        self.screem.title("VOCABULARYZER BY LOKO")
        self.screem.geometry(f"{self._w}x{self._h}")
        self.canvas['width'] = self._w
        self.canvas['height'] = self._h
        self.canvas.place(x=0, y=0)

        self.lblBannerProgram.place(x=self._w * 0.01, y=self._h * 0.01)
        self.lblVocabularyVr.place(x=self._w * 0.01, y=self._h * 0.1)
        self.cmbxVocabularyFiles.place(x=self._w * 0.08, y=self._h * 0.1)

        self.canvas.create_line(0, self._h * 0.15, self._w, self._h * 0.15)
        self.canvas.create_line(self._w * 0.28, self._h * 0.15, self._w * 0.28, self._h * 0.7)
        self.canvas.create_line(0, self._h * 0.7, self._w, self._h * 0.7)

        self.lblSemanticFieldsTitle.place(x=self._w * 0.01, y=self._h * 0.18)
        self.btnAddSemanticDimension.place(x=self._w * 0.17, y=self._h * 0.17)
        
        self.lblFooterProgram.place(x=self._w * 0.44, y=self._h * 0.96)
        self.screem.mainloop()

    def saveAll(self):
        pass

    def setSemanticDimsension(self):
        _title = self.txtTitleSemanticDimension.get()
        _contexIterators = self.txtTitleIteratorsContextual.get()
        _textSDimenDescript = self.txtSemanticDimensionDescription.get()

        if self._isEmptyText(_title):
            self.txtTitleSemanticDimension["bg"] = "red"
            return
        else:
            self.txtTitleSemanticDimension["bg"] = "white"

        if self._isEmptyText(_contexIterators):
            self.txtTitleIteratorsContextual["bg"] = "red"
            return
        else:
            self.txtTitleIteratorsContextual["bg"] = "white"

        if self._isEmptyText(_textSDimenDescript):
            self.txtSemanticDimensionDescription["bg"] = "red"
            return
        else:
            self.txtSemanticDimensionDescription["bg"] = "white"

        self.controller.setSemanticDimsension(_title, _contexIterators, _textSDimenDescript)
        self.showSemanticDimensions()
        self.hideDimensionSemanticInFooter()


    def showDimensionSemanticInFooter(self):
        self.lblTitleSemanticDimension.place(x=self._w * 0.01, y=self._h * 0.72)
        self.txtTitleSemanticDimension.place(x=self._w * 0.22, y=self._h * 0.722)
        self.lblTitleIteratorsContextual.place(x=self._w * 0.01, y=self._h * 0.78)
        self.txtTitleIteratorsContextual.place(x=self._w * 0.22, y=self._h * 0.782)
        self.lblSemanticDimensionDescription.place(x=self._w * 0.01, y=self._h * 0.84)
        self.txtSemanticDimensionDescription.place(x=self._w * 0.22, y=self._h * 0.842)
        self.btnSaveSemanticDimension.place(x=self._w * 0.9, y=self._h * 0.75)

    def showSemanticDimensions(self):
        for w in self._tempSemanticDimensionsOptions:
            w.destroy()
        self._tempSemanticDimensionsOptions.clear()

        _x = self._w * 0.01
        _y_start = self._h * 0.23
        _row_h = 28

        y = _y_start
        for dim in self.controller.semanticDimensionsArr:
            title = dim.name
            btn = Button(self.canvas, text=title, width=26, anchor="w")
            self._tempSemanticDimensionsOptions.append(btn)
            btn.place(x=_x, y=y)
            y += _row_h
    
    def hideDimensionSemanticInFooter(self):
        self.lblTitleSemanticDimension.place_forget()
        self.txtTitleSemanticDimension.place_forget()
        self.lblTitleIteratorsContextual.place_forget()
        self.txtTitleIteratorsContextual.place_forget()
        self.lblSemanticDimensionDescription.place_forget()
        self.txtSemanticDimensionDescription.place_forget()
        self.btnSaveSemanticDimension.place_forget()

    def _isEmptyText(self, txt):
        return str(txt).strip() == ""


s = Software()
