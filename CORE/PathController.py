"""
FelipedelosH
2025

Generate a Paths to Save&Read files
"""
class PathController:
    def __init__(self, path, timeUtil):
        self.path = path
        self.timeUtil = timeUtil

    def getPathByCODE(self, code):
        if code == "DIARY_CURRENT_YYYY":
            return f"{self.path}\\DATA\\DIARIO\\{self.timeUtil.getCurrentYYYY()}\\"
        if code == "DREAM_CURRENT_YYYY":
            return f"{self.path}\\DATA\\DREAMS\\{self.timeUtil.getCurrentYYYY()}\\"
        elif code == "FEELING_CURRENT_YYYY":
            return f"{self.path}\\DATA\\SENTIMIENTOS\\{self.timeUtil.getCurrentYYYY()}\\"
        elif code == "DRUGS_CURRENT_YYYY":
            return f"{self.path}\\DATA\\DRUGS\\{self.timeUtil.getCurrentYYYY()}\\"
        elif code == "ECONOMY_TACCOUNTS_CURRENT_YYYY":
            return f"{self.path}\\DATA\\ECONOMIA\\{self.timeUtil.getCurrentYYYY()}\\"
        elif code == "USAGES":
            return f"{self.path}\\DATA\\USOS\\"
