"""
FelipedelosH
2025

Main Controller
"""
class MainController:
    def __init__(self, dependencies: dict):
        self.dependencies = dependencies

    def save_diary_page(self, path: str, content: str):
        self.dependencies["diary_service"].save_page(path, content)
