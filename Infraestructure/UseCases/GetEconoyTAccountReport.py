"""
FelipedelosH
2025
"""
from Application.UseCases.IGetEconoyTAccountReport import IGetEconoyTAccountReport
from Application.Services.IEconomyService import IEconomyService
from Domain.Entities.Response import Response

class GetEconoyTAccountReport(IGetEconoyTAccountReport):
    def __init__(self, economy_service : IEconomyService):
        self.economy_service = economy_service

    def execute(self, path: str) -> Response:
        return self.economy_service.get_economy_taccount_report(path)
