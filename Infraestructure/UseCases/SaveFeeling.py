"""
FelipedelosH
2025
"""
from Application.UseCases.ISaveFeeling import ISaveFeeling
from Application.Services.IFeelingService import IFeelingService

class SaveFeeling(ISaveFeeling):
    def __init__(self, service: IFeelingService):
        self.feeling_service = service

    def execute(self, path: str, content: str) -> bool:
        return self.feeling_service.save_feeling(path, content)
