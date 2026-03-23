"""
FelipedelosH
2025

Generate a Paths to Save&Read files
"""
from Domain.Enums.PathEnums import PathEnums

class PathController:
    def __init__(self, path, timeUtil):
        self.path = path
        self.timeUtil = timeUtil

    def getPathByCODE(self, code):
        if code == "DIARY":
            return f"{self.path}\\DATA\\DIARIO\\"
        if code == "DIARY_CURRENT_YYYY":
            return f"{self.path}\\DATA\\DIARIO\\{self.timeUtil.getCurrentYYYY()}\\"
        elif code == "DREAM_CURRENT_YYYY":
            return f"{self.path}\\DATA\\DREAMS\\{self.timeUtil.getCurrentYYYY()}\\"
        elif code == "FEELING_CURRENT_YYYY":
            return f"{self.path}\\DATA\\SENTIMIENTOS\\{self.timeUtil.getCurrentYYYY()}\\"
        elif code == "DRUGS":
            return f"{self.path}\\DATA\\DRUGS\\"
        elif code == "DRUGS_CURRENT_YYYY":
            return f"{self.path}\\DATA\\DRUGS\\{self.timeUtil.getCurrentYYYY()}\\"
        elif code == "ECONOMY":
            return f"{self.path}\\DATA\\ECONOMIA\\"
        elif code == "ECONOMY_TACCOUNTS":
            return f"{self.path}\\DATA\\ECONOMIA\\TACCOUNTS\\"
        elif code == "ECONOMY_TACCOUNTS_CURRENT_YYYY":
            return f"{self.path}\\DATA\\ECONOMIA\\TACCOUNTS\\{self.timeUtil.getCurrentYYYY()}\\"
        elif code == "ECONOMY_DEBIT_CURRENT_YYYY":
            return f"{self.path}\\DATA\\ECONOMIA\\DEBITOS\\{self.timeUtil.getCurrentYYYY()}\\"
        elif code == "ECONOMY_DEBIT":
            return f"{self.path}\\DATA\\ECONOMIA\\DEBITOS\\"
        elif code == "SCHELUDED_24_H":
            return f"{self.path}\\DATA\\DISTRIBUCIONTIEMPO\\TIEMPODIARIO\\"
        elif code == "SCHELUDED_24_H_CURRENT_YYYY":
            return f"{self.path}\\DATA\\DISTRIBUCIONTIEMPO\\TIEMPODIARIO\\{self.timeUtil.getCurrentYYYY()}\\"
        elif code == "TEMP":
            return f"{self.path}\\DATA\\TEMP\\"
        elif code == "USAGES":
            return f"{self.path}\\DATA\\USOS\\"
        
    def getPathByCodeAndYYYY(self, code, YYYY):
        if code == "ECONOMY_DEBIT":
            return f"{self.getPathByCODE(code)}{YYYY}\\"
        # ...

    def getAllBasePathInArr(self):
        return [
            self.getPathByCODE(str(PathEnums.DIARY)),
            self.getPathByCODE(str(PathEnums.ECONOMY))
        ]
    
    def getAllBasePathInDict(self):
        return {
            str(PathEnums.DIARY): self.getPathByCODE(str(PathEnums.DIARY)),
            str(PathEnums.SCHELUDED_24_H): self.getPathByCODE(str(PathEnums.SCHELUDED_24_H)),
            str(PathEnums.DRUGS): self.getPathByCODE(str(PathEnums.DRUGS)),
            str(PathEnums.ECONOMY): self.getPathByCODE(str(PathEnums.ECONOMY))
        }
