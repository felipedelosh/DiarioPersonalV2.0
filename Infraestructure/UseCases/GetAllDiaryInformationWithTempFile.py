"""
FelipedelosH
2026
"""
from Application.UseCases.IGetAllDiaryInformationWithTempFile import IGetAllDiaryInformationWithTempFile
from Application.Services.IBackupService import IBackupService
from Application.UseCases.IGetAllPersonalDiaryInformation import IGetAllPersonalDiaryInformation
from Domain.Enums.PathEnums import PathEnums
from Domain.Entities.Response import Response

class GetAllDiaryInformationWithTempFile(IGetAllDiaryInformationWithTempFile):
    def __init__(self, personal_diary_use_case: IGetAllPersonalDiaryInformation, backup_service: IBackupService):
        self.diary_get_all_use_case = personal_diary_use_case
        self.backup_service = backup_service

    def execute(self, pathdict, path_backup_file, backup_file_header_template: str) -> Response:
        _data_backup = ""
        _final_data = {}

        try:
            qty = 0

            _path = pathdict[str(PathEnums.DIARY)]
            _all_data = self.diary_get_all_use_case.execute(_path)

            if _all_data["success"] and _all_data["qty"] > 0:
                _data_backup = _data_backup + str(backup_file_header_template).replace("<TITLE>", str(PathEnums.DIARY)) + "\n"
                _final_data[str(PathEnums.DIARY)] = {}
                for i in _all_data["data"]:
                    _title = str(i)
                    _content = _all_data["data"][_title]
                    _data_backup = _data_backup + f"Title: {_title}\n" + f"Text: {_content}\n" + "*"*40 + "\n"
                    _final_data[str(PathEnums.DIARY)][_title] = _content
                    qty = qty + 1

            _path = pathdict[str(PathEnums.SCHELUDED_24_H)]
            _all_data = self.diary_get_all_use_case.execute(_path)

            if _all_data["success"] and _all_data["qty"] > 0:
                _data_backup = _data_backup + str(backup_file_header_template).replace("<TITLE>", str(PathEnums.SCHELUDED_24_H)) + "\n"
                _final_data[str(PathEnums.SCHELUDED_24_H)] = {}
                for i in _all_data["data"]:
                    _date = str(i)
                    _content = _all_data["data"][_date]
                    _data_backup = _data_backup + f"Date: {_date}\n" + f"Text: {_content}\n" + "."*40 + "\n"
                    _final_data[str(PathEnums.SCHELUDED_24_H)][_date] = _content
                    qty = qty + 1

            _path = pathdict[str(PathEnums.DRUGS)]
            _all_data = self.diary_get_all_use_case.execute(_path)


            if _all_data["success"] and _all_data["qty"] > 0:
                _data_backup = _data_backup + str(backup_file_header_template).replace("<TITLE>", str(PathEnums.SCHELUDED_24_H)) + "\n"
                _final_data[str(PathEnums.DRUGS)] = {}
                for i in _all_data["data"]:
                    _key = str(i)
                    _drug = _key.split(" - ")[0]
                    _date = _key.split(" - ")[1]
                    _date = str(_date).replace(".txt", "")
                    _content = _all_data["data"][_key]

                    _detonation = str(_content).split("\n\n\n")[0]
                    _effect = str(_content).split("\n\n\n")[1]
                    _data_backup = _data_backup + f"DRUG: {_drug}\n" + f"Date: {_date}\n" + f"Detonate: {_detonation}\n" + f"Effect: {_effect}\n" + "-"*40 + "\n"
                    _final_data[str(PathEnums.DRUGS)][_key] = _content
                    qty = qty + 1

            if qty > 0:
                _backup_file = self.backup_service.save(path_backup_file, _data_backup)

            return Response.response(True, _final_data, qty)
        except:
            return Response.response(False, {}, -1)
