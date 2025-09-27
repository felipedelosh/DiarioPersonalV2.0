"""
FelipedelosH
2025

MAIN WINDOW
"""
import tkinter as tk
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
        self.controller = controller
        self.root = tk.Tk()
        self.sideBar = tk.Canvas(self.root, bg="red", highlightthickness=0)
        self.sideBarButtons = []
        self._content_x = 0
        self.content = tk.Canvas(self.root, bg="blue", highlightthickness=0)
        self.manager = ScreenManager(self.root, self.sideBar, self.content, self.controller)
        self.title_app = controller.dependencies["config"].get("title_app")
        self.w = self.controller.dependencies["config"].get("window_w")
        self.h = self.controller.dependencies["config"].get("window_h")
        self.registerWindows()
        self.configureMainWindow()
        self.current_view = None
        self.manager.show("index", self._content_x, 0)

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
        self._configureSideBar()
        self._configureContent()

    def _configureSideBar(self):
        self.sideBar["width"] = self.controller.dependencies["config"].get("window_w") * 0.3
        self.sideBar["height"] = self.controller.dependencies["config"].get("window_h")
        self.sideBar.place(x=0, y=0)

        _counter_btn = 0
        _x0 = int(self.sideBar["width"]) * 0.1
        _btnW = int(self.sideBar["width"]) * 0.8
        _dy = self.controller.dependencies["config"].get("window_h") / len(self.manager._screen_classes)
        for itterOption in self.manager._screen_classes:
            btn = tk.Button(self.sideBar, text=itterOption, command=lambda opt=itterOption: self.show_view(opt))
            self.sideBarButtons.append(btn)
            self.sideBarButtons[_counter_btn].place(x=_x0, y=(_dy * (_counter_btn)) + 10, width=_btnW)

            _counter_btn = _counter_btn + 1


    def _configureContent(self):
        self._content_x = self.controller.dependencies["config"].get("window_w") * 0.3
        self.content["width"] = self.controller.dependencies["config"].get("window_w") - self._content_x
        self.content["height"] = self.controller.dependencies["config"].get("window_h")

    def show_view(self, option):
        print(option)

    def run(self):
        self.root.mainloop()
