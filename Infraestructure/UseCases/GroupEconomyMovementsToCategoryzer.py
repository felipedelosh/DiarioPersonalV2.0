"""
FelipedelosH
2026
"""
from Application.UseCases.IGetAllInformationEconomy import IGetAllInformationEconomy
from Application.Services.IFolderService import IFolderService
from Application.Services.IDebitServive import IDebitService
from Domain.Entities.Response import Response

class GetAllInformationEconomy(IGetAllInformationEconomy):
    def __init__(self, folder_service: IFolderService, debit_service: IDebitService):
        self.folder_service = folder_service
        self.debit_service = debit_service

    def execute(self,  base_path: str) -> Response:
        try:
            _qty = 0
            _data = {}
            _economyFolders = self.folder_service.get_all_folders_in_path(base_path)

            for itterEconomyFolder in _economyFolders["data"]:
                _base_path_economy = f"{base_path}{_economyFolders["data"][itterEconomyFolder]}\\"
                _economyFolderPeerYear = self.folder_service.get_all_folders_in_path(_base_path_economy)

                if _economyFolderPeerYear["success"] and _economyFolderPeerYear["qty"] > 0:
                    for itterEconomyFolderPeerYear in _economyFolderPeerYear["data"]:
                        YYYY = _economyFolderPeerYear["data"][itterEconomyFolderPeerYear]
                        _economyInfoPeerYear = self.debit_service.get_all_debit_path_report_by_year(_base_path_economy, YYYY)

                        if not _economyInfoPeerYear["success"] or not _economyInfoPeerYear["qty"]:
                            continue

                        for itterEconomyData in _economyInfoPeerYear["data"]:
                            print(itterEconomyData)
                            _qty = _qty + 1

            return Response.response(True, _data, _qty)
        except:
            return Response.response(False, {}, -1)