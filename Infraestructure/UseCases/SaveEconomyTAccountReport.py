"""
FelipedelosH
2025
"""
from Application.Services.IEconomyService import IEconomyService
from Application.UseCases.ISaveEconomyTAccountReport import ISaveEconomyTAccountReport

class SaveEconomyTAccountReport(ISaveEconomyTAccountReport):
    def __init__(self, economy_service: IEconomyService):
        self.economy_service = economy_service

    def execute(self, path, content):
        return self.economy_service.save_economy_taccount_report(path, content)
