    """
    FelipedelosH
    2026
    """
    from datetime import datetime
    from Application.Services import IScheduleService
    from Application.UseCases.IGetAllFilesInPath import IGetAllFilesInPath
    from Application.UseCases.IGetSchedulePredictionByDay import IGetSchedulePredictionByDay
    from Application.UseCases.IGetAllFoldersInPath import IGetAllFoldersInPath

    from Domain.Entities.Response import Response

    class GetSchedulePredictionByDay(IGetSchedulePredictionByDay):
        def __init__(self, folder_use_case: IGetAllFoldersInPath, files_use_case: IGetAllFilesInPath, schedule_service: IScheduleService):
            self.folder_use_case = folder_use_case
            self.files_use_case = files_use_case
            self.schedule_service = schedule_service

        def execute(self, path: str, dayNumber: int) -> Response:
            try:
                _qty = 0
                _data = {}
                _data_folders = self.folder_use_case.execute(path)
                if not _data_folders["success"]:
                    return Response.response(False, {}, 0)
                
                years = list(_data_folders["data"].values())
                last_two_years = years[-2:]

                for itterYYYY in last_two_years:
                    _specify_path = f"{path}{itterYYYY}"
                    
                    _all_data = self.files_use_case.execute(_specify_path, ".txt")

                    # FILTER BY DAY
                    if not _all_data["success"] or _all_data["qty"] == 0:
                        continue

                    for itterDfilePath in _all_data["data"]:
                        _date = str(itterDfilePath).replace(".txt", "")
                        _date = _date.split(" ")

                        YYYY = int(_date[0])
                        MM = int(_date[1])
                        DD = int(_date[2])

                        _whatDayIs = datetime(YYYY, MM, DD).weekday()

                        if _whatDayIs != dayNumber:
                            continue

                        _day_data_activities_path = f"{_specify_path}/{itterDfilePath}"
                        _24h_data = self.schedule_service.get_24h_report(_day_data_activities_path)

                        if not _24h_data["success"] or _24h_data["qty"] == 0:
                            continue

                        _24h_data = _24h_data["data"] # {'key': 'value'}
                        _24h_data = list(_24h_data.values())[0]

                        for itterActivity in str(_24h_data).split("\n"):
                            if str(itterActivity).strip() != "":
                                _keyHH = itterActivity.split(":")[0]
                                _valueActivity = itterActivity.split(":")[1]

                                if _keyHH not in _data.keys():
                                    _data[_keyHH] = {}

                                if _valueActivity not in _data[_keyHH].keys():
                                    _data[_keyHH][_valueActivity] = 1
                                else:
                                    _data[_keyHH][_valueActivity] = _data[_keyHH][_valueActivity] + 1

                                _qty = _qty + 1

                return Response.response(True, _data, _qty)
            except:
                return Response.response(False, {}, -1)
