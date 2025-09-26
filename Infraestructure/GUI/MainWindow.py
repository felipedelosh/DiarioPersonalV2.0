"""
FelipedelosH
2025

MAIN WINDOW
"""
import tkinter as tk
from Infraestructure.GUI.ScreenManager import ScreenManager
from Infraestructure.GUI.views.DiaryView import DiaryView
from Infraestructure.GUI.views.FinancesView import FinancesView
from Infraestructure.GUI.views.GraphsView import GraphsView
from Infraestructure.GUI.views.ChatbotView import ChatbotView
from Infraestructure.GUI.views.SettingsView import SettingsView

class MainWindow:
    def __init__(self, controller):
        self.title_app = controller.dependencies["config"].get("title_app")
        self.w = controller.dependencies["config"].get("window_w")
        self.h = controller.dependencies["config"].get("window_h")
        self.root = tk.Tk()
        self.root.title(self.title_app)
        self.root.geometry(f"{self.w}x{self.h}")

        self.manager = ScreenManager(self.root, controller)

        # Registrar pantallas
        self.manager.add("diary", DiaryView)
        self.manager.add("finances", FinancesView)
        self.manager.add("graphs", GraphsView)
        self.manager.add("chatbot", ChatbotView)
        self.manager.add("settings", SettingsView)

        # Mostrar pantalla inicial
        self.manager.show("diary")

    def run(self):
        self.root.mainloop()
