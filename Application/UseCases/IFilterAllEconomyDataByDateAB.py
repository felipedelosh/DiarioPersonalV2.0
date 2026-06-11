"""
FelipedelosH
2026

Enter a Economy All Response {
    success: bool
    qty: number
    data: dict
}

take all key file name in dic 'path'/YYYY/MM_NAME DD.csv and detenerminate is between date.
"""
from abc import ABC, abstractmethod
from Domain.Entities.Response import Response

class IFilterAllEconomyDataByDateAB(ABC):
    @abstractmethod
    def execute(self, response_data: Response, dateA: str, dateB: str, mm_names: list) -> Response:
        pass
