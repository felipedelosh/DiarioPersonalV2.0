"""
FelipdelosH
2025

Time Utils
"""
import time
from datetime import date

class TimeUtils:
    def __init__(self):
        self.durationMMinDays = [31,28,31,30,31,30,31,31,30,31,30,31]

    def getCurrentYYYY(self):
        return date.today().year
    
    def getCurrentMM(self):
        return date.today().month
    
    def getNumberOfDaysInXMM(self, mm):
        return self.durationMMinDays[mm]
    
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

    def getStrHHByCounter(self, start, counter_value):
        """
        Enter a counter (0-23) represents 24 HH peer day, and Enter a start HH slices by counter
        Example start: 6 (be 06:00am) if counter_value: 3 returns 8am
        
        :param start: first hour of day
        :param counter_value: Slicer
        """
        _HH_STAR = start 
        _isAM = True
        hour_str = ""

        for _ in range(counter_value + 1):
            if _HH_STAR == 13:
                _HH_STAR = 1
                _isAM = not _isAM

            _TT_ = "am" if _isAM else "pm"
            hour_str = f"{_HH_STAR}{_TT_}"

            _HH_STAR += 1


        return hour_str

