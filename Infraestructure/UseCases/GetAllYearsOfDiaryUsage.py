"""
FelipedelosH
2026
"""
from Application.UseCases.IGetAllYearsOfDiaryUsage import IGetAllYearsOfDiaryUsage
from Application.Services.IFolderService import IFolderService
from Domain.Entities.Response import Response

class GetAllYearsOfDiaryUsage(IGetAllYearsOfDiaryUsage):
    def __init__(self, service_folder: IFolderService):
        self.service_folder = service_folder

    def execute(self,  path_dict: dict) -> Response:
        try:
            _YYYY = []
            for i in path_dict:
                _base_path = path_dict[i]
    
                _data = self.service_folder.get_all_folders_in_path(_base_path)
                
                if not _data["success"] or _data["qty"] <= 0:
                    continue

                for keyData in _data["data"]:
                    _yData = _data["data"][keyData]
                    
                    try:
                        YYYY = int(_yData)

                        if YYYY > 2000:
                            if YYYY not in _YYYY:
                                _YYYY.append(YYYY)
                    except:
                        continue

            if not _YYYY:
                return Response.response(False, {}, -1)
            
            _YYYY.sort()
            _final_data = {}
            _counter = 0
            for i in _YYYY:
                _final_data[_counter] = i
                _counter = _counter + 1

            return Response.response(True, _final_data, _counter)
        except:
            return Response.response(False, {}, -1)
