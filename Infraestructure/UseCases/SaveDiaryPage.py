"""
FelipedelosH
2025
"""
from Application.UseCases.ISaveDiaryPage import ISaveDiaryPage
from Application.Services.IDiaryService import IDiaryService

class SaveDiaryPage(ISaveDiaryPage):
    def __init__(self, diary_service: IDiaryService):
        self.diary_service = diary_service

    def save_page(self, path: str, content: str) -> None:
        self.diary_service.save_page(path, content)
