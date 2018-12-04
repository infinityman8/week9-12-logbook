class CashRegister:
    def __init__(self):
        self._itemCount=0
        self._totalPrice=0.0

    def addItem(self,price):
        self._totalPrice=self._itemCount + 1
        self._totalPrice=self._totalPrice + price

    def getTotal(self):
        return self._totalPrice

    def getCount(self):
        return self._itemCount

    def clear(self):
        self._itemCount = 0
        self._totalPrice = 0.0

    def giveChange(self, payment):
        self._totalPrice
        payment._totalPrice

register1 = CashRegister()
print(register1._itemCount, register1._totalPrice)

