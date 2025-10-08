"""
FelipedelosH
2025
"""
import os
from os import scandir
from Domain.Entities.Response import Response

class FileReader:
    def __init__(self):
        pass

    def getFileDataFromKeyword(self, path, keyword):
        """
        Return the first concidence with keyword name of file
        """
        try:
            _file = ""
            _filemame = ""
            for i in scandir(path):
                if i.is_file():
                    if str(keyword).lower() in str(i.name).lower():
                        _file = i.path
                        _filemame = i.name

            if not _file:
                return Response.response(False, {}, -1)
            
            _content = ""
            with open(_file, "r", encoding="UTF-8") as f:
                _content = f.read()

            data = {
                "title": _filemame,
                "content": _content
            }

            return Response.response(True, data, 1)
        except:
            return Response.response(False, {}, -1)
