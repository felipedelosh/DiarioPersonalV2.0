"""
FelipedelosH
2026

Generates a VOCABULARY FILE to FEMPUTADORA
KEY = [#, ...#]
"""
from tkinter import *
from controller import *

class Software:
    def __init__(self) -> None:
        self._w = 720
        self._h = 480
        self.controller = Controller()
        self.screem = Tk()
        self.canvas = Canvas(self.screem)
        self.lblBannerProgram = Label(self.canvas, text="Generates a file to FEMPUTADORA VOCABULARY...")
        self.lblFooterProgram = Label(self.canvas, text="FelipedelosH")


        self.vizualizedAndRun()


    def vizualizedAndRun(self):
        self.screem.title("VOCABULARYZER BY LOKO")
        self.screem.geometry(f"{self._w}x{self._h}")
        self.canvas['width'] = self._w
        self.canvas['height'] = self._h
        #self.canvas['bg'] = "snow"
        self.canvas.place(x=0, y=0)
        self.lblBannerProgram.place(x=self._w * 0.01, y=self._h * 0.01)
        self.lblFooterProgram.place(x=self._w * 0.42, y=self._h * 0.9)


        self.screem.mainloop()




s = Software()
