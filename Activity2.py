class Computer:
    def __init__(self):
        self.__maxprice=1200
    def sell(self):
        print("Selling price:",self.__maxprice)
    def setmaxprice(self, price):
        self.__maxprice=price
c=Computer()
c.sell()
c.__maxprice=1299
c.sell()
c.setmaxprice(1299)
c.sell()
