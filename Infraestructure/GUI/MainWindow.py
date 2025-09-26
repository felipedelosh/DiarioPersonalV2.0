"""
FelipedelosH
2025

MAIN WINDOW
"""
import tkinter as tk
from tkinter import ttk
from Infraestructure.GUI.ScreenManager import ScreenManager
from Infraestructure.GUI.views.DiaryView import DiaryView
from Infraestructure.GUI.views.CalendarView import CalendarView
from Infraestructure.GUI.views.FinancesView import FinancesView
from Infraestructure.GUI.views.GraphsView import GraphsView
from Infraestructure.GUI.views.ChatbotView import ChatbotView
from Infraestructure.GUI.views.SettingsView import SettingsView

class MainWindow:
    def __init__(self, controller):
        self.root = tk.Tk()
        self.title_app = controller.dependencies["config"].get("title_app")
        self.w = controller.dependencies["config"].get("window_w")
        self.h = controller.dependencies["config"].get("window_h")
        self.manager = ScreenManager(self.root, controller)

        # Display elements
        self.sidebar = tk.Frame(self.root, bg="#ffffff", width=200)
        self.sidebarTitle = tk.Label(self.sidebar, text="Diario")
        self.sidebarButtons = {}
        
        self.registerWindows()
        self.configureMainWindow()
        self.current_view = None
        self.manager.show("diary")

    def registerWindows(self):
        self.manager.add("diary", DiaryView)
        self.manager.add("calendar", CalendarView)
        self.manager.add("finances", FinancesView)
        self.manager.add("graphs", GraphsView)
        self.manager.add("chatbot", ChatbotView)
        self.manager.add("settings", SettingsView)

    def configureMainWindow(self):
        # SideBar
        self.sidebar.pack(side="left", fill="y")
        self.sidebarTitle.pack(pady=20)
        options = self.manager.screens
        for opt in options:
            btn = tk.Button(self.sidebar, text=opt, font=("Arial", 12),
                            bg="#f1f1f7", fg="#333333",
                            relief="flat", activebackground="#dcdcf5",
                            command=lambda o=opt: self.show_view(o))
            btn.pack(fill="x", pady=5, padx=10, ipady=8)
            self.sidebarButtons[opt] = btn

        # ======= Contenedor de vistas =======
        self.container = tk.Frame(self.root, bg="#f9f9fb")
        self.container.pack(side="right", expand=True, fill="both")
        # END TEST NEW GRAPHICS
        self.root.title(self.title_app)
        self.root.geometry(f"{self.w}x{self.h}")

    def show_view(self, name):
        # Destruir vista anterior
        if self.current_view:
            self.current_view.destroy()

        # Crear una nueva vista (simulada)
        self.current_view = tk.Frame(self.container, bg="#f9f9fb")
        self.current_view.pack(expand=True, fill="both")

        label = tk.Label(self.current_view, text=f"Vista: {name}",
                         font=("Arial", 18), bg="#f9f9fb", fg="#333333")
        label.pack(pady=50)

        # Ejemplo: botón dentro de cada vista
        tk.Button(self.current_view, text=f"Abrir {name}",
                  bg="#4c6ef5", fg="white", font=("Arial", 12, "bold"),
                  relief="flat", padx=10, pady=5).pack()

    def run(self):
        self.root.mainloop()
