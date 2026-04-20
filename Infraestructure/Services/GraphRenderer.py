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
        if graphicsType == str(GraphType.PIE_TACCOUNTS_ALL):
            self._renderAllTAccountsInPIEGraphic(canvas, data)

        if graphicsType == str(GraphType.BAR_TACCOUNTS_ALL):
            self._renderAllTAccountsInBarGraphic(canvas, data)

        if graphicsType == str(GraphType.CARTESIAN_TACCOUNTS_LINES_PLOTTER):
            self._renderAllTAccountsInLinePLotterGraphic(canvas, data, options)

    def _renderAllTAccountsInPIEGraphic(self, canvas: Canvas, data: Response):
        """
        Enter All TAccounts information {'path': 'data'}

        Divide Screm In TWO PARTS (Debit, Credit)... and PUT PIE
        """
        # VARS
        w = float(canvas["width"])
        h = float(canvas["height"])
        initAnge = 0
        endAngle = 0
        _total_cash = 0
        _total_debit = 0 # IN
        _total_credit = 0 # OUT
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
        _margin = w * 0.04
        _circleTOP = h * 0.9
        _textMarginX = w * 0.72
        _textMarginY = h * 0.2
        canvas.create_oval(_margin, _margin, _circleTOP, _circleTOP, fill="azure", width=3)

        # [COLOR, $$$]
        dataToPaint = {
            "IN": ["green", _total_debit],
            "OUT": ["red", _total_credit]
        }

        if _total_cash != 0:
            _counter = 0
            for i in dataToPaint:
                _name = i
                _color = dataToPaint[i][0]
                _value = dataToPaint[i][1]

                endAngle = 360 * (_value/_total_cash)
                canvas.create_arc(_margin, _margin, _circleTOP, _circleTOP, width=1, fill=_color, start=initAnge, extent=endAngle)
                canvas.create_text(_textMarginX, _textMarginY + (20 * _counter), fill = _color, text=_name + " : " + f"{self.format_money(_value)}")
                initAnge = initAnge + endAngle
                _counter = _counter + 1

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

    def _renderAllTAccountsInLinePLotterGraphic(self, canvas: Canvas, data: Response, options):
        """
        Enter All TAccounts information: {YYYY: {'FILE_PATH': 'DATA'} }
        """
        arrYYYY = sorted([int(i) for i in data["data"].keys()])

        # Calculate margins & paint AREAS.
        _w_left_margin, _w_right_margin, _h_bottom_margin, _h_top_margin, w, h = self._renderAllTAccountsInLinePLotterGraphicGetPlotDimensions(canvas)
        
        # Paint Aixis
        x0 = _w_left_margin
        y0 = _h_bottom_margin
        x1 = _w_right_margin
        y1 = _h_top_margin
        self._renderAllTAccountsInLinePLotterGraphicPaintAixis(canvas, x0, y0, x1, y1)

        # VARS: Util Painted AREA
        lineW = x1 - x0
        #print(f"Total area util X: {lineW}")
        lineH = y0 - y1
        #print(f"Total area util Y: {lineH}")

        _totalYears = len(data["data"])
        #print(f"Total de años: {_totalYears}")
        if _totalYears > 0:
            dLineW = lineW / _totalYears
            self._renderAllTAccountsInLinePLotterGraphicDrawYYYYDividers(canvas, _totalYears, arrYYYY, _w_left_margin, _h_bottom_margin, dLineW)
            _maxTAccountDebitValue, _maxTAccountCreditValue = self._renderAllTAccountsInLinePLotterGraphicGetMaxDebitAndCredit(data)
            dataToPaint = self._renderAllTAccountsInLinePLotterGraphicVectorizeAndOrderDateInformation(data, options)

            _prevDebitPoint = (_w_left_margin, _h_bottom_margin)
            for itterTAccountFile in dataToPaint:
                for k, v in itterTAccountFile.items():
                    _dateExtract = str(k).split("/")

                    _YYYY = int(_dateExtract[0])
                    _MM = int(_dateExtract[1])
                    _DD = int(_dateExtract[2])


                    x = self._renderAllTAccountsInLinePLotterGraphicGetPointXByDate(_YYYY, _MM, _DD, arrYYYY, dLineW)

                    _debit = 0
                    _credit = 0
                    for i in str(v).split("\n"):
                        if str(i).strip() != "":
                            _TAccountData = str(i).split(";")

                            _tempDebit = float(_TAccountData[1])
                            _debit = _debit + _tempDebit
                            _tempCredit = float(_TAccountData[2])
                            _credit = _credit + _tempCredit
                    
                    # PAINT DEBIT
                    x0 = _w_left_margin + x
                    ratio = _debit / _maxTAccountDebitValue
                    if ratio > 0.1:
                        y0 = _h_bottom_margin - ((_debit / _maxTAccountDebitValue) * lineH)

                        canvas.create_line(
                            _prevDebitPoint[0], _prevDebitPoint[1],
                            x0, y0,
                            fill="green",
                            width=2
                        )
                        canvas.create_oval(x0 - 2, y0 - 2, x0 + 2, y0 + 2, fill="green")
                        _prevDebitPoint = (x0, y0)
                    #print(f"Para el registro: {_YYYY, _MM, _DD} IN: {_debit} <> OUT: {_credit}")

                    # PAINT CREDIT


    def _renderAllTAccountsInLinePLotterGraphicGetPlotDimensions(self, canvas):
        w = float(canvas["width"])
        h = float(canvas["height"])
        left = w * 0.05
        right = w * 0.95
        bottom = h * 0.9
        top = h * 0.1
        return left, right, bottom, top, w, h
    def _renderAllTAccountsInLinePLotterGraphicPaintAixis(self, canvas, x0, y0, x1, y1):
        canvas.create_line(x0, y0, x1, y0, width=2, arrow="last")# X
        canvas.create_line(x0, y0, x0, y1, width=2, arrow="last")# Y
    def _renderAllTAccountsInLinePLotterGraphicDrawYYYYDividers(self, canvas, _totalYears, arrYYYY, _w_left_margin, _h_bottom_margin, dLineW):
        for i in range(_totalYears):
            divider_x = _w_left_margin + (i * dLineW)
            divider_y0 = _h_bottom_margin - 5
            divider_y1 = _h_bottom_margin + 5

            text_x = divider_x + (dLineW / 3)
            text_y = _h_bottom_margin + 15
            canvas.create_text(text_x, text_y, text=str(arrYYYY[i]))

            if i != 0:
                canvas.create_line(divider_x, divider_y0, divider_x, divider_y1, width=2)
    def _renderAllTAccountsInLinePLotterGraphicGetMaxDebitAndCredit(self, data):
        _maxTAccountDebitValue = 0 # IN
        _maxTAccountCreditValue = 0 # OUT
        for itterYYYY in data["data"]:
            for itterTAccountFile in data["data"][itterYYYY]:
                for i in str(data["data"][itterYYYY][itterTAccountFile]).split("\n"):
                    if str(i).strip() != "":
                        _TAccountData = str(i).split(";")
                        _debit = float(_TAccountData[1])
                        _credit = float(_TAccountData[2])

                        if _maxTAccountDebitValue < _debit:
                            _maxTAccountDebitValue = _debit

                        if _maxTAccountCreditValue < _credit:
                            _maxTAccountCreditValue = _credit

        return _maxTAccountDebitValue, _maxTAccountCreditValue
    def _renderAllTAccountsInLinePLotterGraphicVectorizeAndOrderDateInformation(self, data, options):
        # Extract relevant info
        information = []
        for itterYYYY in data["data"]:
            for itterTAccountFile in data["data"][itterYYYY]:
                _dateExtract = str(itterTAccountFile).split("TACCOUNTS")[1]
                _dateExtract = str(_dateExtract).replace(".csv", "")
                _dateExtract = str(_dateExtract).replace("/", " ")
                _dateExtract = str(_dateExtract).replace("\\", "")
                _dateExtract = str(_dateExtract).split(" ")  # [YYYY, MMName, DD]

                _MMNames = options["MMNames"]
                _dateExtract[1] = _MMNames.index(_dateExtract[1]) + 1

                _YYYY = int(_dateExtract[0])
                _MM = int(_dateExtract[1])
                _DD = int(_dateExtract[2])

                information.append({f"{_YYYY}/{_MM}/{_DD}": data["data"][itterYYYY][itterTAccountFile]})

        
        # order BubbleShort
        n = len(information)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                key1 = list(information[j].keys())[0]
                key2 = list(information[j + 1].keys())[0]
                
                def get_date_tuple(key):
                    y, m, d = key.split('/')
                    return (int(y), int(m), int(d))
                
                date1 = get_date_tuple(key1)
                date2 = get_date_tuple(key2)
                
                if date1 > date2:
                    information[j], information[j + 1] = information[j + 1], information[j]

        return information
    def _renderAllTAccountsInLinePLotterGraphicGetPointXByDate(self, YYYY, MM, DD, arrYYYY, dw):
        """
        Enter a DATE and calculate position with YYYY spacing
        """
        x = 0

        _yearIndex = arrYYYY.index(YYYY)
        x = dw * _yearIndex
        
        dMonthW = dw / 12
        _monthIndex = MM - 1
        x = x + (dMonthW * _monthIndex)

        dDayW = dMonthW / 30
        _dayIndex = DD - 1
        x = x + (dDayW * _dayIndex)
        
        return x
