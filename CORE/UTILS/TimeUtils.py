"""
FelipdelosH
2025

Time Utils
"""
import time
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
    
    def getCurrentHHMMSS(self):
        _time = str(time.ctime()).split(" ")
        _time = _time[-2]

        return _time
    
    def getNumberOfCurrentDD(self):
        return date.today().weekday()
    
    def getTimeStamp(self):
        return str(self.getCurrentYYYY()) + " " + str(self.getCurrentMM()) + " " + str(self.getCurrentDD())
    
    def getTimeSignature(self):
        return str(time.ctime())
