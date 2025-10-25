"""
FelipedelosH
2025
"""
from Application.Services.IEconomyService import IEconomyService
from Application.Repositories.IEconomyRepository import IEconomyRepository

class EconomyService(IEconomyService):
    def __init__(self, economy_repository: IEconomyRepository):
        self.economy_repository = economy_repository

    def save_economy_taccount_report(self, path: str, content: str) -> bool:
        return self.economy_repository.save_economy_taccount_report(path, content)
