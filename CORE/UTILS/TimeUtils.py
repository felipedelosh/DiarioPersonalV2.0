"""
FelipdelosH
2025

Time Utils
"""
from datetime import date

class TimeUtils:
    def __init__(self):
        pass

    def getCurrentYYYY(self):
        return date.today().year
    
    def getCurrentMM(self):
        return date.today().month
    
    def getCurrentDD(self):
        return date.today().day
    
    def getNumberOfCurrentDD(self):
        return date.today().weekday()
    
    def getTimeStamp(self):
        return str(self.getCurrentYYYY()) + " " + str(self.getCurrentMM()) + " " + str(self.getCurrentDD())
