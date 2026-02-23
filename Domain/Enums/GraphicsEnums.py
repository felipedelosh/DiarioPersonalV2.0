"""
FelipdelosH
2026
"""
from enum import Enum
from enum import auto

class GraphType(Enum):
    # Economy
    PIE_TACCOUNTS_ALL = auto()
    PIE_DEBITS_ALL = auto()
    BAR_TACCOUNTS_ALL = auto()
    BAR_TACCOUNTS_FILTERED_BY_TIME = auto()
    BAR_TACCOUNTS_FILTERED_BY_CATEGORY = auto()
    BAR_DEBITS_ALL = auto()
    CARTESIAN_ZZZ_VS_MONEY = auto()
    # ...
