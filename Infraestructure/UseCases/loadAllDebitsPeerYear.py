"""
FelipedelosH
2025
"""
from Application.UseCases.ILoadAllDebitsPeerYear import ILoadAllDebitsPeerYear
from Application.Services.IDebitServive import IDebitService
from Domain.Entities.Response import Response

class LoadAllDebitsPeerYear(ILoadAllDebitsPeerYear):
    def __init__(self, debit_service: IDebitService):
        self.debit_service = debit_service

    def execute(self,  path: str, YYYY: str) -> Response:
        return self.debit_service.get_all_debit_path_report_by_year(path, YYYY)
