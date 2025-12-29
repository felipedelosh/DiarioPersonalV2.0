"""
FelipedelosH
2025
"""
from abc import ABC, abstractmethod
from Domain.Entities.Response import Response

class IDebitService(ABC):
    @abstractmethod
    def save_debit_report(self, path: str, content: str) -> bool:
        pass

    @abstractmethod
    def save_pay_debit_report(self, path: str, content: str) -> bool:
        pass

    @abstractmethod
    def get_all_debit_path_report_by_year(self, path: str, YYYY: str) -> Response:
        pass

    @abstractmethod
    def register_debit_payment(self, path: str, content: str) -> bool:
        pass
