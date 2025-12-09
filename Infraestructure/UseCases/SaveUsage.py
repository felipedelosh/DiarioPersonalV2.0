"""
FelipedelosH
2025
"""
from Application.UseCases.ISaveUsagesUseCase import ISaveUsage
#from Application.Services.

class SaveUsage(ISaveUsage):
    def __init__(self):
        pass

    def execute(self, path: str, timeStamp: str) -> bool:
        return True
