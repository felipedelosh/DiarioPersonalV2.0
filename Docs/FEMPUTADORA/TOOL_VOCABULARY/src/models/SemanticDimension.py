"""
FelipdelosH
2026
"""

class SemanticDimensión:
    def __init__(self, id, name, contextualIteratorsArr, description):
        self.id = id
        self.name = name
        self.contextualIteratorsArr = contextualIteratorsArr
        self.description = description

    def __str__(self):
        return f"{self.name} >> {str(self.contextualIteratorsArr)}"
