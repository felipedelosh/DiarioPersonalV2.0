"""
FelipedelosH
2025
"""
from Application.Services.IDiaryService import IDiaryService
from Application.Repositories.IDiaryRepository import IDiaryRepository

class DiaryService(IDiaryService):
    def __init__(self, diary_repo: IDiaryRepository):
        self.diary_repo = diary_repo

    def save_page(self, path: str, content: str) -> None:
        self.diary_repo.save_diary_page(path, content)