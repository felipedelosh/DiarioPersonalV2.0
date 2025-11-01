"""
FelipedelosH
2025

Standard respose for REQUEST

success = bool
data = data
qty = len of data
"""
class Response:
    def __init__(self, success: bool, data: dict | None = None, qty = 0):
        self.success = success
        self.data = data
        self.qty = qty

    @staticmethod
    def response(success: bool, data: dict | None = None, qty = 0):
        return {
            "success": success,
            "qty": qty,
            "data": data
        }
