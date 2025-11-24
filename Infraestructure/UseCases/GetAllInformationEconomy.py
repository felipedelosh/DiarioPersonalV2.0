"""
FelipedelosH
2025
"""
from Application.UseCases.IGetAllInformationEconomy import IGetAllInformationEconomy
from Application.Services.IFolderService import IFolderService
from Application.Services.IDebitServive import IDebitService
from Domain.Entities.Response import Response

class GetAllInformationEconomy(IGetAllInformationEconomy):
    def __init__(self, folder_service: IFolderService, debit_service: IDebitService):
        self.folder_service = folder_service
        self.debit_service = debit_service

    def execute(self,  base_path: str, keyword: str, initDate: str, finalDate: str) -> Response:
        try:
            # WIP
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
                            process = self.processEconomyInformation(_base_path_economy, YYYY, _data, itterEconomyData, _economyInfoPeerYear["data"])

                            if process:
                                _qty = _qty + 1

            return Response.response(True, _data, _qty)
        except:
            return Response.response(False, {}, -1)
        
    def processEconomyInformation(self, path, YYYY, data, keyEconomyMovement, EconomyMovement):
        try:
            # DATE|CONCEPT|CASH|TYPE|STATUS
            if "DEBITOS" in path:
                keyWord = f"DEBIT-{keyEconomyMovement}"
                _dataSplited = str(EconomyMovement[keyEconomyMovement]).split("|")

                date = str(keyEconomyMovement).split(" ")
                MM = date[1]
                DD = date[2]
                date = f"{YYYY}/{MM}/{DD}"
                concept = _dataSplited[4]
                _max_length = 40
                if len(concept) > _max_length:
                    concept = concept[:_max_length - 3] + "..."
                cash = _dataSplited[1]
                status = _dataSplited[5]

                info = f"{date}|{concept}|{cash}|DEBIT|{status}"
                data[keyWord] = info

                return True

            if "TACCOUNTS" in path:
                keyWord = f"TACCOUNT-{keyEconomyMovement}"
                _dataSplited = str(EconomyMovement[keyEconomyMovement]).split(";")

                date = str(keyEconomyMovement).split(".")[0]
                MM, DD = str(date).split(" ")
                date = f"{YYYY}/{MM}/{DD}"

                concept = _dataSplited[0]
                _max_length = 40
                if len(concept) > _max_length:
                    concept = concept[:_max_length - 3] + "..."

                cash = ""
                status = ""
                if _dataSplited[1] == "0":
                    status = "DEBIT"
                    cash = _dataSplited[2]
                else:
                    status = "CREDIT"
                    cash = _dataSplited[1]

                info = f"{date}|{concept}|{cash}|TACCOUNT|{status}"
                data[keyWord] = info

                return True

            return False
        except:
            return False
