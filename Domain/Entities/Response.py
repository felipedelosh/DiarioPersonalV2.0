"""
FelipedelosH
2025

Standard respose for REQUEST

success = bool
data = data
qty = len of data
"""
class Response:
    def __init__(self, success: bool, data: dict | None = None, qty = 0, pagination: dict | None = None):
        self.success = success
        self.data = data
        self.qty = qty
        self.pagination = pagination

    @staticmethod
    def response(success: bool, data: dict | None = None, qty = 0):
        return {
            "success": success,
            "qty": qty,
            "data": data
        }
    
    @staticmethod
    def responsePaginated(success: bool, data: dict | None = None, qty = 0, pagination: dict | None = None):
        return {
            "success": success,
            "qty": qty,
            "data": data,
            "pagination": pagination
        }
