"""
FelipedelosH
2026
"""
from Application.UseCases.IChatWithFemputadora import IChatWithFemputadora
from CORE.FEMPUTADORA.Femputadora import Femputadora
from Domain.Entities.Response import Response

class ChatWithFemputadora(IChatWithFemputadora):
    def __init__(self, femputadora: Femputadora):
        self.femputadora = femputadora

    def execute(self, txt) -> Response:
        response = self.femputadora.getResponse(txt)
        return Response.response(True, {"text" : response}, 1)
