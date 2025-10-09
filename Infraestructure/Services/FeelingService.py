"""
FelipedelosH
2025
"""
from Application.Services.IFeelingService import IFeelingService
from Application.Repositories.IFeelingRepository import IFeelingRepository

class FeelingService(IFeelingService):
    def __init__(self, feeling_repo: IFeelingRepository):
        self.feeling_repo = feeling_repo

    def save_feeling(self, path: str, content: str) -> bool:
        return self.feeling_repo.save_feeling(path, content)
