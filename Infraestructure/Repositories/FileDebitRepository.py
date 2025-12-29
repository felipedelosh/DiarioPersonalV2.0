"""
FelipedelosH
2025
"""
from Application.Repositories.IDebitRepository import IDebitRepository
from Infraestructure.Persistence.FileWriter import FileWriter
from Infraestructure.Persistence.FileReader import FileReader
from Domain.Entities.Response import Response

class FileDebitRepository(IDebitRepository):
    def __init__(self):
        self.file_writer = FileWriter()
        self.file_reader = FileReader()

    def save_debit_report(self, path: str, content: str) -> bool:
        return self.file_writer.saveFile(path, content)
    
    def save_pay_debit_report(self, path: str, content: str) -> bool:
        return self.file_writer.overWritefile(path, content)
    
    def get_all_debit_path_report_by_year(self, path: str, YYYY: str) -> Response:
        _path = f"{path}{YYYY}"
        return self.file_reader.getAllFilesInPathByExt(_path, ".csv")
    
    def register_debit_payment(self, path: str, content: str) -> bool:
        return self.file_writer.overWritefile(path, content)
