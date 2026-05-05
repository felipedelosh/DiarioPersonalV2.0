"""
FelipedelosH
2025
"""
from Application.UseCases.IGetAllFoldersInPath import IGetAllFoldersInPath
from Application.Services.IFolderService import IFolderService
from Domain.Entities.Response import Response

class GetAllFilesInPath(IGetAllFoldersInPath):
    def __init__(self, folder_service: IFolderService):
        self.folder_service = folder_service

    def execute(self, path, ext) -> Response:
        _data = self.folder_service.get_all_files_in_path_by_ext(path, ext)
        return _data
