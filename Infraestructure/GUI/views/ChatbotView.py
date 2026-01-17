"""
FelipedelosH
2025
"""
import tkinter as tk
from Infraestructure.GUI.Screen import Screen

class ChatbotView(Screen):
    def render(self, x, y):
        self.canvas["bg"]="black"
        self.canvas.place(x=x, y=y)
        self._w = float(self.canvas["width"])
        self._h =float(self.canvas["height"])
        self.lang = self.manager.controller.dependencies["lang"]
        self.stringProcesor = self.manager.controller.utils["string_procesor"]
        self._tempCurrentElementsOptions = [] # TO DELETE AFTER USE OR CHANGE VIEW

        self.renderFemputadoraView()

    def renderFemputadoraView(self):
        txtEntry = tk.Entry(self.canvas, fg="gray")
        txtEntry.insert(0, self.lang.getText("femputadora_txt_input"))
        txtEntry.bind("<FocusIn>", lambda e, entry=txtEntry: self._clear_placeholder_entry_text(entry))
        txtEntry.bind("<FocusOut>", lambda e, entry=txtEntry: self._add_placeholder_entry_text(entry))
        txtEntry.bind("<Return>", lambda e, entry=txtEntry: self._on_enter_pressed(entry))
        self._tempCurrentElementsOptions.append(txtEntry)
        txtEntry.place(x=self._w*0.07, y=self._h*0.3, width=self._w*0.5, height=25)

    def _clear_placeholder_entry_text(self, entry):
        if entry.get() == self.lang.getText("femputadora_txt_input"):
            entry.delete(0, tk.END)
            entry.config(fg="black")
    def _add_placeholder_entry_text(self, entry):
        if not entry.get():
            entry.insert(0, self.lang.getText("femputadora_txt_input"))
            entry.config(fg="gray")

    def _on_enter_pressed(self, entry):
        text = entry.get().strip()

        if not text or text == self.lang.getText("femputadora_txt_input"):
            return

        _data = self.manager.controller.dependencies["chat_femputadora_use_case"].execute(text)

        print("Usuario escribió:", text)
        print("==================")
        print("Respuesta: ", _data)
        entry.delete(0, tk.END)
