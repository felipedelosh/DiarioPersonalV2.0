"""
FelipedelosH
2025
"""
from Application.UseCases.ILoadDiaryPage import ILoadDiaryPage
from Application.Services.IDiaryService import IDiaryService
from Domain.Entities.Response import Response

class LoadDiaryPage(ILoadDiaryPage):
    def __init__(self, diary_service: IDiaryService):
        self.diary_service = diary_service

    def execute(self, path: str, content: str) -> Response:
        return self.diary_service.load_page(path, content)
