"""
FelipedelosH
2025

Standard respose for REQUEST
"""
class Response:
    def __init__(self, success: bool, data: dict | None = None, status_code: int = 200):
        self.success = success
        self.data = data
        self.status_code = status_code

    @staticmethod
    def response(success: bool, data: dict | None = None, status_code: int = 200):
        return {
            "success": success,
            "statusCode": status_code,
            "data": data
        }
