"""
FelipedelosH
2026
"""
from Application.UseCases.IGetAllDiaryInformationWithTempFile import IGetAllDiaryInformationWithTempFile
from Domain.Enums.PathEnums import PathEnums
from Domain.Entities.Response import Response

class GetAllDiaryInformationWithTempFile(IGetAllDiaryInformationWithTempFile):
    def __init__(self):
        pass

    def execute(self, pathdict, path_backup_file, backup_file_header_template: str) -> Response:
        _data_backup = ""
        print(pathdict)
        print(path_backup_file)
        print(backup_file_header_template)

        try:
            qty = 0

            _path = pathdict[str(PathEnums.DIARY)]
            
            print("Entraa....")
            print(_path)

            return Response.response(True, {}, qty)
        except:
            return Response.response(False, {}, -1)