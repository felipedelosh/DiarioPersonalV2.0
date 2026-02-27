"""
FelipedelosH
2025
"""
from Application.UseCases.IPayDebit import IPayDebit
from Application.Services.IDebitServive import IDebitService

class PayDebit(IPayDebit):
    def __init__(self, debit_service: IDebitService):
        self.debit_service = debit_service

    def execute(self, path, content, date, comment, state):
        try:
            _debitInfoArr = str(content).split("\n")
            _mainDebit = _debitInfoArr[0]

            _UUID = str(_mainDebit).split("|")[0]
            _total = str(_mainDebit).split("|")[1]
            _total = float(_total)
            _interest = str(_mainDebit).split("|")[2]
            _interest = float(_interest)

            if _interest > 0:
                _total = _total * (1 + (_interest/100))

            _balance = _total
            

            print(len(_debitInfoArr))

            if len(_debitInfoArr) > 1:
                _total_balance_payments = 0

                for itterDebit in _debitInfoArr[1::]:
                    _data = str(itterDebit).split("|")
                    _total_balance_payments = _total_balance_payments + float(_data[1])

                _rest = _balance + _total_balance_payments
                last_pay = f"{_UUID}|{_rest * -1}|{_interest}|{date}|{comment}|{state}"
            else:
                if _balance <= 0:
                    return False
                
                last_pay = f"{_UUID}|{_balance * -1}|{_interest}|{date}|{comment}|{state}"
                
            _newMainDebit = ""
            _mainDebit = str(_mainDebit).split("|")
            _mainDebit[-1] = state
            for itterMainDebit in _mainDebit:
                _newMainDebit = _newMainDebit + itterMainDebit + "|"
            _newMainDebit = _newMainDebit[:-1]
            _debitInfoArr[0] = _newMainDebit
            _debitInfoArr.append(last_pay)

            _pay_report = ""
            for itterDebitData in _debitInfoArr:
                _pay_report = _pay_report + itterDebitData + "\n"
            _pay_report = _pay_report[:-1]

            return self.debit_service.save_pay_debit_report(path, _pay_report)
        except:
            return False
