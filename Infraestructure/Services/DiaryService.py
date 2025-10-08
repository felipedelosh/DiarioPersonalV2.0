"""
FelipedelosH
2025
"""
from Application.Services.IDiaryService import IDiaryService
from Application.Repositories.IDiaryRepository import IDiaryRepository
from Domain.Entities.Response import Response

class DiaryService(IDiaryService):
    def __init__(self, diary_repo: IDiaryRepository):
        self.diary_repo = diary_repo

    def save_page(self, path: str, content: str) -> bool:
        return self.diary_repo.save_diary_page(path, content)
    
    def load_page(self, path: str, keyword: str) -> Response:
        return self.diary_repo.load_diary_page(path, keyword)