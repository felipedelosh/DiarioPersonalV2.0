"""
FelipedelosH
2025
"""
from Application.UseCases.ILoadAllDebitsYearsRegistered import ILoadAllDebitsYearsRegistered
from Application.UseCases.IGetAllFoldersInPath import IGetAllFoldersInPath
from Application.UseCases.ILoadAllDebitsPeerYear import ILoadAllDebitsPeerYear
from Domain.Entities.Response import Response

class LoadAllDebitsYearsRegistered(ILoadAllDebitsYearsRegistered):
    def __init__(self, folder_use_case: IGetAllFoldersInPath, debits_peer_year_use_case: ILoadAllDebitsPeerYear):
        self.folder_use_case = folder_use_case
        self.debits_peer_year_use_case = debits_peer_year_use_case

    def execute(self, path) -> Response:
        try:
            _dataDebitFolders = self.folder_use_case.execute(path)

            if not _dataDebitFolders["success"]:
                return Response.response(False, {}, 0)

            _output = {}
            _counter = 0
            for YYYY in _dataDebitFolders["data"].values():
                _data = self.debits_peer_year_use_case.execute(path, YYYY)

                if not _data["success"]:
                    continue

                _counter = _counter + _data["qty"]
                _output = _output | _data["data"]

            return Response.response(True, _output, _counter)
        except:
            return Response.response(False, {}, 0)
