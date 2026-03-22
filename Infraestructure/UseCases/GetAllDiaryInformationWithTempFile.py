"""
FelipedelosH
2026
"""
from Application.UseCases.IGetAllDiaryInformationWithTempFile import IGetAllDiaryInformationWithTempFile
from Domain.Enums.PathEnums import PathEnums
from Application.UseCases.IGetAllPersonalDiaryInformation import IGetAllPersonalDiaryInformation
from Domain.Entities.Response import Response

class GetAllDiaryInformationWithTempFile(IGetAllDiaryInformationWithTempFile):
    def __init__(self, personal_diary_use_case: IGetAllPersonalDiaryInformation):
        self.personal_diary_get_all_use_case = personal_diary_use_case

    def execute(self, pathdict, path_backup_file, backup_file_header_template: str) -> Response:
        _data_backup = ""

        try:
            qty = 0

            _path = pathdict[str(PathEnums.DIARY)]
            _all_data = self.personal_diary_get_all_use_case.execute(_path)
            
            print("Entraa....")
            print(_path)
            print(_all_data)

            return Response.response(True, {}, qty)
        except:
            return Response.response(False, {}, -1)