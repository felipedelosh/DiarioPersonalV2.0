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
                            process = self.processEconomyInformation(_base_path_economy, YYYY, _data, itterEconomyData, _economyInfoPeerYear["data"], keyword, initDate, finalDate, _qty)

                            if process:
                                _qty = _qty + 1

            return Response.response(True, _data, _qty)
        except:
            return Response.response(False, {}, -1)
        
    def processEconomyInformation(self, path, YYYY, data, keyEconomyMovement, EconomyMovement, keyword, initDate, finalDate, baseFolderCounter):
        try:
            # DATE|CONCEPT|CASH|TYPE|STATUS
            if "DEBITOS" in path:
                keyWord = f"DEBIT-{keyEconomyMovement}"
                _rows = len(str(EconomyMovement[keyEconomyMovement]).split("\n"))

                if _rows == 0:
                    _dataSplited = str(EconomyMovement[keyEconomyMovement]).split("|")
                else:
                    _dataSplited = str(EconomyMovement[keyEconomyMovement]).split("\n")[0]
                    _dataSplited = str(_dataSplited).split("|")

                date = str(keyEconomyMovement).split(" ")
                MM = date[1]
                DD = date[2]
                date = f"{YYYY}/{MM}/{DD}"
                concept = _dataSplited[4]

                # FILTERS
                if self.filter(concept, date, keyword, initDate, finalDate):
                    return False
                # FILTERS

                cash = _dataSplited[1]
                status = _dataSplited[5]

                info = f"{date}|{concept}|{cash}|DEBIT|{status}"
                data[keyWord] = info

                return True
            
            # DATE|CONCEPT|CASH|TYPE|STATUS
            if "TACCOUNTS" in path:
                _regCounter = 0
                for itterTAcc in str(EconomyMovement[keyEconomyMovement]).split("\n"):
                    if str(itterTAcc).strip() == "":
                        continue
                
                    _dataSplited = str(itterTAcc).split(";")

                    date = str(keyEconomyMovement).split(".")[0]
                    MM, DD = str(date).split(" ")
                    date = f"{YYYY}/{MM}/{DD}"

                    concept = _dataSplited[0]

                    # FILTERS
                    if self.filter(concept, date, keyword, initDate, finalDate):
                        continue
                    # FILTERS

                    cash = ""
                    status = ""
                    if _dataSplited[1] == "0":
                        status = "DEBIT"
                        cash = _dataSplited[2]
                    else:
                        status = "CREDIT"
                        cash = _dataSplited[1]

                    keyWord = f"TACCOUNT-{baseFolderCounter}-{_regCounter}-{keyEconomyMovement}"
                    info = f"{date}|{concept}|{cash}|TACCOUNT|{status}"
                    data[keyWord] = info
                    _regCounter = _regCounter + 1

                # Add info?
                return _regCounter != 0

            return False
        except Exception as e:
            print(f"ERROR::USE_CASE::GET_ALL_INFORMATION_ECONOMY::{str(e)}")
            return False
        
    def filter(self, InputConcetp, InputDate, FilterKeyword, FilterInitDate, FilterFinalDate):
        """
        Return True if Match With Filters

        InputConcetp: TEXT
        InputDate: YYYY/MM/DD
        """
        if FilterKeyword != "":
            if not str(FilterKeyword).lower() in str(InputConcetp).lower():
                return True
            
        if InputDate != "" and FilterInitDate != "":
            _dataTimeInput = str(InputDate).split("/")
            _dataTimeInputYYYY = int(_dataTimeInput[0])

            _dataTimeFilter = str(FilterInitDate).split("/")
            _dataTimeFilterYYYY = int(_dataTimeFilter[0])

            if _dataTimeInputYYYY < _dataTimeFilterYYYY:
                return True
            
        if InputDate != "" and FilterFinalDate != "":
            _dataTimeInput = str(InputDate).split("/")
            _dataTimeInputYYYY = int(_dataTimeInput[0])

            _dataTimeFilter = str(FilterFinalDate).split("/")
            _dataTimeFilterYYYY = int(_dataTimeFilter[0])

            if _dataTimeInputYYYY > _dataTimeFilterYYYY:
                return True

        return False
