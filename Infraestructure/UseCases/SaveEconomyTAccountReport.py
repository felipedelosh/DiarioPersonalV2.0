"""
FelipedelosH
2025
"""
from Application.Services.IEconomyService import IEconomyService
from Application.UseCases.ISaveEconomyTAccountReport import ISaveEconomyTAccountReport
from Application.UseCases.IGetEconoyTAccountReport import IGetEconoyTAccountReport

class SaveEconomyTAccountReport(ISaveEconomyTAccountReport):
    def __init__(self, economy_service: IEconomyService, economy_use_case_get_taccount: IGetEconoyTAccountReport):
        self.economy_service = economy_service
        self.economy_use_case_get_taccount = economy_use_case_get_taccount

    def execute(self, path, content):
        _dataExistsPreviuosInfo = self.economy_use_case_get_taccount.execute(path)

        if _dataExistsPreviuosInfo["success"] and _dataExistsPreviuosInfo["qty"] > 0:
            _previousData = _dataExistsPreviuosInfo["data"]
            _previousData = next(iter(_previousData.values()))
            _futureData = f"{_previousData}\n{content}"

            return self.economy_service.update_economy_taccount_report(path, _futureData)

        return self.economy_service.save_economy_taccount_report(path, content)
