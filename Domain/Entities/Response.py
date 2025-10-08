"""
FelipedelosH
2025

Standard respose for REQUEST
"""
class Response:
    def __init__(self, success: bool, data: dict | None = None, status = 0):
        self.success = success
        self.data = data
        self.status = status

    @staticmethod
    def response(success: bool, data: dict | None = None, status = 0):
        return {
            "success": success,
            "statusCode": status,
            "data": data
        }
