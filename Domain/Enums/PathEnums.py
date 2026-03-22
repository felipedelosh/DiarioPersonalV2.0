"""
FelipdelosH
2026
"""
from enum import Enum
from enum import auto

class PathEnums(Enum):
    DIARY = auto()
    ECONOMY = auto()

    def __str__(self):
        return self.name
