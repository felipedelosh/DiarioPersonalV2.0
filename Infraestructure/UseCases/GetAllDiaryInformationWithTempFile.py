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

    def execute(self, pathdict, path_backup_file) -> Response:
        print(pathdict)
        print(path_backup_file)

        return Response.response(False, {}, 0)