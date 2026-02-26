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
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "contextualIteratorsArr": self.contextualIteratorsArr,
            "description": self.description
        }

    @staticmethod
    def from_dict(d):
        return SemanticDimensión(
            d.get("id"),
            str(d.get("name", "")).upper(),
            [str(x).strip().lower() for x in d.get("contextualIteratorsArr", [])],
            d.get("description", "")
        )
