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
        # VARS
        self._chat_history = [] 
        self._txt_chat = ""
        self._display_mode = ""

        self.renderFemputadoraView()

    def renderFemputadoraView(self):
        self.draw_femputadora_face()
        _state = self.manager.controller.dependencies["config"].get("fempuadora_mode")

        if self._display_mode == _state[0]:
            self.deleteOption()
            self.draw_femputadora_question_mode()
        elif self._display_mode == _state[1]:
            self.deleteOption()
            self.draw_femputadora_chat_mode()
        elif self._display_mode == _state[2]:
            self.deleteOption()
            self.draw_femputadora_graphics_mode()
        else:
            self.deleteOption()
            self.draw_femputadora_question_mode()
    def deleteOption(self):
        for widget in self._tempCurrentElementsOptions:
            widget.destroy()
        self._tempCurrentElementsOptions.clear()

    def draw_femputadora_face(self):
        pass

    def draw_femputadora_question_mode(self):
        lblWelcomeMessage = tk.Label(self.canvas ,text = self.lang.getText("femputadora_help"), bg="black",fg="red")
        self._tempCurrentElementsOptions.append(lblWelcomeMessage)
        lblWelcomeMessage.place(x=self._w * 0.42, y=self._h * 0.42)

        txtEntry = tk.Entry(self.canvas, fg="gray")
        txtEntry.insert(0, self.lang.getText("femputadora_txt_input"))
        txtEntry.bind("<FocusIn>", lambda e, entry=txtEntry: self._clear_placeholder_entry_text(entry))
        txtEntry.bind("<FocusOut>", lambda e, entry=txtEntry: self._add_placeholder_entry_text(entry))
        txtEntry.bind("<Return>", lambda e, entry=txtEntry: self._on_enter_pressed(entry))
        self._tempCurrentElementsOptions.append(txtEntry)
        txtEntry.place(x=self._w * 0.26, y=self._h * 0.5, width=self._w * 0.5, height=25)

    def draw_femputadora_chat_mode(self):
        txtChat = tk.Text(self.canvas, width=74, height=25, wrap="word")
        self._tempCurrentElementsOptions.append(txtChat)
        txtChat.place(x=self._w*0.06, y=self._h*0.12)

        txtEntry = tk.Entry(self.canvas, fg="gray")
        txtEntry.insert(0, self.lang.getText("femputadora_txt_input"))
        txtEntry.bind("<FocusIn>", lambda e, entry=txtEntry: self._clear_placeholder_entry_text(entry))
        txtEntry.bind("<FocusOut>", lambda e, entry=txtEntry: self._add_placeholder_entry_text(entry))
        txtEntry.bind("<Return>", lambda e, entry=txtEntry: self._on_enter_pressed(entry))
        self._tempCurrentElementsOptions.append(txtEntry)
        txtEntry.place(x=self._w * 0.06, y=self._h * 0.85, width=self._w * 0.88, height=23)

        self._render_chat(txtChat)

    def draw_femputadora_graphics_mode(self):
        pass

    def _clear_placeholder_entry_text(self, entry):
        if entry.get() == self.lang.getText("femputadora_txt_input"):
            entry.delete(0, tk.END)
            entry.config(fg="black")
    def _add_placeholder_entry_text(self, entry):
        if not entry.get():
            entry.insert(0, self.lang.getText("femputadora_txt_input"))
            entry.config(fg="gray")

    def _on_enter_pressed(self, entry):
        _mode = self.manager.controller.dependencies["config"].get("env")
        text = entry.get().strip()

        if not text or text == self.lang.getText("femputadora_txt_input"):
            return

        _data = self.manager.controller.dependencies["chat_femputadora_use_case"].execute(text)
        _femputadora_data = _data["data"]
        _new_chat = f"{'User'}:\n{text}\n\n"

        

        if _mode == "DEV":
            _new_chat = _new_chat + f"{'Femputadora'}:\n"

            for i in _femputadora_data:
                _new_chat = _new_chat + f"\n{i}:\n{_femputadora_data[i]}"
        else:
            pass

        self._txt_chat = self._txt_chat + _new_chat
        _state = self.manager.controller.dependencies["config"].get("fempuadora_mode")
        self._display_mode = _state[1]
        entry.delete(0, tk.END)
        self.renderFemputadoraView()

    def _render_chat(self, txtEntry):
        txtEntry.delete("1.0", tk.END)
        txtEntry.insert(tk.END, self._txt_chat)
