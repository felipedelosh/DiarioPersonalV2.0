"""
FelipedelosH
2025
"""
from Application.UseCases.ISaveDreamPage import ISaveDreamPage
from Application.Services.IDreamService import IDreamService

class SaveDreamPage(ISaveDreamPage):
    def __init__(self, dream_service: IDreamService):
        self.dream_service = dream_service

    def execute(self, path: str, content: str) -> bool:
        return self.dream_service.save_dream(path, content)
