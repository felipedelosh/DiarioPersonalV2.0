"""
FelipedelosH
2025
"""
from Application.Services.IFeelingService import IFeelingService
from Application.Repositories.IFeelingRepository import IFeelingRepository
from Domain.Entities.Response import Response

class FeelingService(IFeelingService):
    def __init__(self, feeling_repo: IFeelingRepository):
        self.feeling_repo = feeling_repo

    def save_feeling(self, path: str, content: str) -> bool:
        return self.feeling_repo.save_feeling(path, content)

    def get_feel_info(self, path: str) -> Response:
        return self.feeling_repo.get_feel_info(path)
