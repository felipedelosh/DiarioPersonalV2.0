"""
FelipedelosH
2025

MAIN WINDOW
"""
import tkinter as tk
from tkinter import ttk
from Infraestructure.GUI.ScreenManager import ScreenManager
from Infraestructure.GUI.views.IndexView import IndexView
from Infraestructure.GUI.views.DiaryView import DiaryView
from Infraestructure.GUI.views.CalendarView import CalendarView
from Infraestructure.GUI.views.FinancesView import FinancesView
from Infraestructure.GUI.views.GraphsView import GraphsView
from Infraestructure.GUI.views.ChatbotView import ChatbotView
from Infraestructure.GUI.views.SettingsView import SettingsView

class MainWindow:
    def __init__(self, controller):
        self.root = tk.Tk()
        self.manager = ScreenManager(self.root, controller)
        self.title_app = controller.dependencies["config"].get("title_app")
        self.w = controller.dependencies["config"].get("window_w")
        self.h = controller.dependencies["config"].get("window_h")
        self.registerWindows()
        self.configureMainWindow()
        self.current_view = None
        self.manager.show("index")

    def registerWindows(self):
        self.manager.add("index", IndexView)
        self.manager.add("diary", DiaryView)
        self.manager.add("calendar", CalendarView)
        self.manager.add("finances", FinancesView)
        self.manager.add("graphs", GraphsView)
        self.manager.add("chatbot", ChatbotView)
        self.manager.add("settings", SettingsView)

    def configureMainWindow(self):
        self.root.title(self.title_app)
        self.root.geometry(f"{self.w}x{self.h}")

    def show_view(self, name):
        pass

    def run(self):
        self.root.mainloop()
