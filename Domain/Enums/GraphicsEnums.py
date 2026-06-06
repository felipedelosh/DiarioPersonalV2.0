"""
FelipdelosH
2026
"""
from enum import Enum
from enum import auto

class GraphType(Enum):
    # Economy
    PIE = auto()
    BAR = auto()
    LINE = auto()
    # ...

    def __str__(self):
        return self.name
