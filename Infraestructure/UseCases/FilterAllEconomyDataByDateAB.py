"""
FelipedelosH
2026
"""
from datetime import datetime
from Application.UseCases.IFilterAllEconomyDataByDateAB import IFilterAllEconomyDataByDateAB
from Domain.Entities.Response import Response

class FilterAllEconomyDataByDateAB(IFilterAllEconomyDataByDateAB):
    def __init__(self):
        pass

    def execute(self, response_data: Response, dateA: str, dateB: str, mm_names: list) -> Response:
        try:
            qty = 0
            _final_data = {}

            if not response_data["success"] or response_data["qty"] < 0:
                return Response.response(False, {}, 0)
            
            _dateA = datetime.strptime(dateA, "%Y/%m/%d")
            _dateB = datetime.strptime(dateB, "%Y/%m/%d")

            if _dateA > _dateB:
                return Response.response(response_data["success"], response_data["data"], response_data["qty"])

            for key, value in response_data["data"].items():
                _date = str(key).split("\\TACCOUNTS\\")[1] # delete path route
                _date = str(_date).replace(".csv", "")
                _YYYY = str(_date).split("/")[0]
                _date = str(_date).split("/")[1]
                _date = str(_date).split(" ")
                _MM_NAME = _date[0]
                _MM = mm_names.index(_MM_NAME) + 1
                _DD = _date[1]

                if _MM_NAME not in mm_names:
                    continue

                _current_date = datetime(
                    int(_YYYY),
                    int(_MM),
                    int(_DD)
                )

                if _dateA <= _current_date <= _dateB:
                    _final_data[key] = value
                    qty = qty + 1

            return Response.response(True, _final_data, qty)
        except:
            return Response.response(response_data["success"], response_data["data"], response_data["qty"])
