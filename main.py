"""
FelipedelosH
2025

PersonalDiaryV2.0
"""
from CORE.MainController import MainController
from CORE.DependencyInjector import DependencyInjector
from Infraestructure.GUI.MainWindow import MainWindow

class Software:
    def __init__(self):
        self.controller = MainController(
            DependencyInjector.build_dependencies(),
            DependencyInjector.build_utils()
        )
        # RUN APP
        self.launch()

    def launch(self):
        app = MainWindow(self.controller)
        app.run()

s = Software()
