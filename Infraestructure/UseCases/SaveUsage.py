"""
FelipedelosH
2025
"""
from Application.UseCases.ISaveUsagesUseCase import ISaveUsage
from Application.Services.IUsageService import IUsageService

class SaveUsage(ISaveUsage):
    def __init__(self, usage_service: IUsageService):
        self.usage_service = usage_service

    def execute(self, path: str, YYYY: str, typeUsage: str, timeStamp: str) -> bool:
        _path = f"{path}{YYYY}-{typeUsage}.txt"
        return self.usage_service.save_usage(_path, timeStamp)
