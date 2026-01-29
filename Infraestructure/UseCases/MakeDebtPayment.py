"""
FelipedelosH
2025
"""
from Application.UseCases.IMakeDebtPayment import IMakeDebtPayment
from Application.Services.IDebitServive import IDebitService

class MakeDebtPayment(IMakeDebtPayment):
    def __init__(self, debit_service: IDebitService):
        self.debit_service = debit_service

    def execute(self, path, content, amount, date, comment):
        try:
            _debitInfoArr = str(content).split("\n")
            _mainDebit = _debitInfoArr[0]

            _UUID = str(_mainDebit).split("|")[0]
            _total = str(_mainDebit).split("|")[1]
            _total = float(_total)
            _interest = str(_mainDebit).split("|")[2]
            _interest = float(_interest)
            _status = str(_mainDebit).split("|")[5]

            if _interest > 0:
                _total = _total * (1 + (_interest/100))

            _balance = _total

            if _balance <= 0:
                return False

            if amount > _balance:
                return False

            # UPDATE INFO OF DEBIT
            _new_content = ""
            for i in _debitInfoArr:
                _new_content = _new_content + f"{i}" + "\n"

            _new_content = _new_content + f"{_UUID}|{amount * -1}|{_interest}|{date}|{comment}|{_status}"
            
            return self.debit_service.register_debit_payment(path, _new_content)
        except:
            return False
