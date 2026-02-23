"""
FelipdelosH
2026

Implementation of Graphier
"""
from tkinter import Canvas
from Domain.Enums.GraphicsEnums import GraphType
from Application.Services.IGraphRenderer import IGraphRenderer
from Domain.Entities.Response import Response

class GraphRenderer(IGraphRenderer):
    def __init__(self):
        pass

    def render(self, canvas: Canvas, data: Response, graphicsType: str, options):
        print("Graphier By LOKO")

        if graphicsType == str(GraphType.BAR_TACCOUNTS_ALL):
            self._renderAllTAccountsInBarGraphic(canvas, data)

    def _renderAllTAccountsInBarGraphic(self, canvas: Canvas, data: Response):
        """
        Enter All TAccounts information {'path': 'data'}

        Divide Screm In TWO PARTS (Debit, Credit)... and PUT BARs
        """
        # VARS
        w = float(canvas["width"])
        h = float(canvas["height"])
        _total_cash = 0
        _total_debit = 0 # IN
        _percent_debit = 0
        _total_credit = 0 # OUT
        _percent_credit = 0
        _TOP_DEBIT = ['', 0]
        _TOP_CREDIT = ['', 0]

        for itterTAccountPath in data["data"]:
            _data = data["data"][itterTAccountPath]
            
            # Calculate MAX & MIN & T
            for itterTAccountData in str(_data).split("\n"):
                if str(itterTAccountData).strip() == "":
                    continue
                
                try:
                    _splited_data = str(itterTAccountData).split(";")
                    _concept = _splited_data[0]
                    _debit = _splited_data[1]
                    _debit = float(_debit)

                    if _debit > _TOP_DEBIT[1]:
                        _TOP_DEBIT = [_concept, _debit]

                    _credit = _splited_data[2]
                    _credit = float(_credit)

                    if _credit > _TOP_CREDIT[1]:
                        _TOP_CREDIT = [_concept, _credit]
                    
                    _total_debit = _total_debit + _debit
                    _total_credit = _total_credit + _credit
                except:
                    continue

        _total_cash = _total_debit + _total_credit
        if _total_cash != 0:
            _percent_debit = _total_debit / _total_cash
            _percent_credit = _total_credit / _total_cash

        # PAINT DEBIT
        x0 = 0 + 4
        y0 = 0 + 4
        x1 = w * _percent_debit + 2
        y1 = h / 10
        canvas.create_rectangle(x0, y0, x1, y1, fill="green")
        canvas.create_text(w / 7, 20, text=self.format_money(_total_debit))
        canvas.create_text(w * 0.35, (h/10)+20, text=f"{_TOP_DEBIT[0]} << ${self.format_money(_TOP_DEBIT[1])}", tags="economia")
        canvas.create_line(0, (h/10)+35, w, (h/10)+35)
        
        # MIDDLE DIVISOR
        canvas.create_line(0, h * 0.5, w, h * 0.5)

        # PAINT CREDIT
        x0 = 0 + 4
        y0 = (h/2) + 4
        x1 = w * _percent_credit + 2
        y1 = (h/2) + (h/10)
        canvas.create_rectangle(x0, y0, x1, y1, fill="red")
        canvas.create_text(w/7, (h/2)+20, text=self.format_money(_total_credit))
        canvas.create_text(w * 0.35, (h/2)+(h/10)+20, text=f"{_TOP_CREDIT[0]} >> ${self.format_money(_TOP_CREDIT[1])}")
        canvas.create_line(0, (h/2)+(h/10)+35, w, (h/2)+(h/10)+35)

    def format_money(self, value: float) -> str:
        value = float(value)
        entero = int(value)
        decimal = abs(value - entero)

        entero_str = f"{entero:,}".replace(",", ".")
        decimal_str = f"{decimal:.2f}".split(".")[1]

        return f"$ {entero_str}.{decimal_str}"

