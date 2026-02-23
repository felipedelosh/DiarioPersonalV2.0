"""
FelipedelosH
2025
"""
from os import scandir
from Application.Services.IFolderService import IFolderService
from Domain.Entities.Response import Response

class FolderService(IFolderService):
    def __init__(self):
        pass

    def get_all_folders_in_path(self, path) -> Response:
        try:
            _folderNames = []

            with scandir(path) as entries:
                for entry in entries:
                    if entry.is_dir():
                        _folderNames.append(entry.name)

            _folderNames.sort()
            _output = {}
            _counter = 0
            for i in _folderNames:
                _output[_counter] = i
                _counter = _counter + 1

            return Response.response(True, _output, _counter)
        except:
            return Response.response(False, {}, 0)
        
    def get_all_files_in_path_by_ext(self, path: str, ext: str) -> Response:
        try:
            file_names = []
            with scandir(path) as entries:
                for entry in entries:
                    if entry.is_file():
                        name = entry.name
                        if not ext or name.lower().endswith(ext):
                            file_names.append(name)

            return Response.response(True, file_names, len(file_names))
        except Exception:
            return Response.response(False, [], 0)
