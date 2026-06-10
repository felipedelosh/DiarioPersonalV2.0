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

class GraphEconomyFilters(Enum):
    # Economy Filters
    TIME_FILTER = auto()
    SLEEP_VS_MONEY = auto()
    CATEGORIES_FILTER = auto()
    # ...

    def __str__(self):
        return self.name
