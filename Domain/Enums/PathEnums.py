"""
FelipdelosH
2026
"""
from enum import Enum
from enum import auto

class PathEnums(Enum):
    DIARY = auto()
    DREAMS = auto()
    SCHELUDED_24_H = auto()
    DRUGS = auto()
    ECONOMY = auto()
    FEELINGS = auto()
    TEMP = auto()

    def __str__(self):
        return self.name
