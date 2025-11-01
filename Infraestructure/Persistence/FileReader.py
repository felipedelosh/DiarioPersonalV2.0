"""
FelipedelosH
2025
"""
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
                        break

            _content = self.getTxtDataOfFile(_file)

            if not _file or not _content:
                return Response.response(False, {}, -1)

            data = {
                "title": _filemame,
                "content": _content
            }

            return Response.response(True, data, 1)
        except:
            return Response.response(False, {}, -1)
        
    def getAllFilesInPathByExt(self, path, ext):
        """
        Return a response: Dict of all files with ext { 'filename0.txt': data0.str }
        """
        try:
            data = {}
            qty = 0

            for i in scandir(path):
                if i.is_file():
                    if ext in i.name:
                        data[i.name] = self.getTxtDataOfFile(i.path)
                        qty = qty + 1

            if not data or qty == 0:
                return Response.response(False, {}, -1)

            return Response.response(True, data, qty)
        except:
            return Response.response(False, {}, -1)

    def getTxtDataOfFile(self, path):
        try:
            with open(path, "r", encoding="UTF-8") as f:
                return f.read()
            
            return None
        except:
            return None
