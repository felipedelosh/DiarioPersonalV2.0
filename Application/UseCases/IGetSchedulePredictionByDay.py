"""
FelipedelosH
2026

Using Law of Large numbers to predict the schedule of a day based on the historical data of the same day in previous two years.
"""
from abc import ABC, abstractmethod
from Domain.Entities.Response import Response

class IGetSchedulePredictionByDay(ABC):
    @abstractmethod
    def execute(self, path: str, dayNumber: int) -> Response:
        pass
