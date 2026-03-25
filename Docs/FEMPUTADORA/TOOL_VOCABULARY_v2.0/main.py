"""
FelipedelosH

TOOL - VOCABULATY

GENERATE & EDIT 'vocabulary_tokenizer_ids.py'
"""
from tkinter import *
from tkinter import ttk
from controller import *

class Software:
    def __init__(self):
        self._w = 900
        self._h = 600
        self.controller = Controller()
        self.screem = Tk()
        self.canvas = Canvas(self.screem)
        self.lblBannerProgram = Label(self.canvas, text="Generates a file to FEMPUTADORA VOCABULARY...")
        self.lblVocabularyVr = Label(self.canvas, text="Versión: ")
        self.lblOption = Label(self.canvas, text="Options")
        self.cmbxVocabularyFiles = ttk.Combobox(self.canvas)
        self.cmbxVocabularyFiles["values"] = self.controller.loadPreviosWorksNameSpaces()
        self.btnLoadWork = Button(self.canvas, text="LOAD WORK", bg="orange", command=self.loadWork)
        self.btnSaveWork = Button(self.canvas, text="SAVE WORK", bg="green", command=self.saveWork)
        self.btnAddNewSemanticDimension = Button(self.canvas, text="ADD Semantic Dimension", command=self.open_add_semantic_dimension_window)
        # Semantic Dimensio Statitics
        self.lblSemanticDimenionCounter = Label(self.canvas, text="Semantic Dimensions: 0")
        
        self.lblFooterProgram = Label(self.canvas, text="FelipedelosH")
        self.vizualizedAndRun()

    def vizualizedAndRun(self):
        self.screem.title("VOCABULARYZER BY LOKO")
        self.screem.geometry(f"{self._w}x{self._h}")
        self.canvas['width'] = self._w
        self.canvas['height'] = self._h
        self.canvas.place(x=0, y=0)
        self.lblBannerProgram.place(x=self._w * 0.01, y=self._h * 0.01)
        self.lblVocabularyVr.place(x=self._w * 0.3, y=self._h * 0.08)
        self.cmbxVocabularyFiles.place(x=self._w * 0.37, y=self._h * 0.08)
        self.btnLoadWork.place(x=self._w * 0.7, y=self._h * 0.05)

        self.lblOption.place(x=self._w * 0.1, y=self._h * 0.2)
        self.btnAddNewSemanticDimension.place(x=self._w * 0.05, y=self._h * 0.26)

        self.canvas.create_line(0, self._h * 0.15, self._w, self._h * 0.15)
        self.canvas.create_line(self._w * 0.28, self._h * 0.15, self._w * 0.28, self._h * 0.7)
        self.canvas.create_line(0, self._h * 0.7, self._w, self._h * 0.7)

        self.showBtnSaveWork()
        
        self.lblFooterProgram.place(x=self._w * 0.44, y=self._h * 0.96)
        self.screem.mainloop()

    def saveWork(self):
        title = self.cmbxVocabularyFiles.get()
        if not self._isEmptyText(title):
            self.controller.savePythonSemanticDimension(title)

    def loadWork(self):
        title = self.cmbxVocabularyFiles.get()
        if not self._isEmptyText(title):
            _status = self.controller.loadPreviousWork(title)

            if _status:
                print(f"OK:LOAD:{title}")
                self.showBtnSaveWork()
                self.showSemanticDimensionStatitics()
            else:
                print(f"ERR:LOAD:{title}")

    def open_add_semantic_dimension_window(self):
        top = Toplevel(self.screem)
        top.title("ADD New Semantic Dimension")
        top.geometry("800x200")
        top.resizable(False, False)

        main_frame = Frame(top)
        main_frame.pack(padx=20, pady=20, fill=BOTH, expand=True)
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)

        Label(main_frame, text="Nombre de dimensión semántica:").grid(row=0, column=0, sticky="e", pady=5)
        txtTitleSemanticDimension = Entry(main_frame, width=80)
        txtTitleSemanticDimension.grid(row=0, column=1, pady=5)

        Label(main_frame, text="Iteradores contextuales (separados por comas):").grid(row=1, column=0, sticky="ne", pady=5)
        txtTitleIteratorsContextual = Entry(main_frame, width=80)
        txtTitleIteratorsContextual.grid(row=1, column=1, pady=5)

        Label(main_frame, text="Descripción:").grid(row=2, column=0, sticky="ne", pady=5)
        txtSemanticDimensionDescription = Entry(main_frame, width=80)
        txtSemanticDimensionDescription.grid(row=2, column=1, pady=5)

        btnGuardar = Button(main_frame, text="Guardar", command= lambda : self.saveSemanticDimension(txtTitleSemanticDimension, txtTitleIteratorsContextual, txtSemanticDimensionDescription, top))
        btnGuardar.grid(row=3, column=0, columnspan=2, pady=20)

    def saveSemanticDimension(self, txtTitleSemanticDimension, txtTitleIteratorsContextual, txtSemanticDimensionDescription, top):
        _title = txtTitleSemanticDimension.get()
        _contexIterators = txtTitleIteratorsContextual.get()
        _textSDimenDescript = txtSemanticDimensionDescription.get()

        if self._isEmptyText(_title):
            txtTitleSemanticDimension["bg"] = "red"
            return
        else:
            txtTitleSemanticDimension["bg"] = "white"

        if self._isEmptyText(_contexIterators):
            txtTitleIteratorsContextual["bg"] = "red"
            return
        else:
            txtTitleIteratorsContextual["bg"] = "white"

        if self._isEmptyText(_textSDimenDescript):
            txtSemanticDimensionDescription["bg"] = "red"
            return
        else:
            txtSemanticDimensionDescription["bg"] = "white"

        self.controller.setNewSemanticDimension(_title, _contexIterators, _textSDimenDescript)
        self.showBtnSaveWork()
        self.showSemanticDimensionStatitics()
        top.destroy()

    def showBtnSaveWork(self):
        if len(self.controller.semanticDimensionsArr) > 0:
            self.btnSaveWork.place(x=self._w * 0.9, y=self._h * 0.05)

    def showSemanticDimensionStatitics(self):
        _data = self.controller.getSemanticDimesionStatitics()
        self.lblSemanticDimenionCounter["text"] = f"Semantic Dimensions: {_data['total']}"
        self.lblSemanticDimenionCounter.place(x=self._w * 0.01, y=self._h * 0.75)

    def _isEmptyText(self, txt):
        return str(txt).strip() == ""

s = Software()
