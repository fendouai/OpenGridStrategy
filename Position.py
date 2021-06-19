class Position(object):
    fund = 0
    stock = 0
    def __init__(self,fund):
        self.fund = fund
        self.stock = 0
        # 上一次买入价
        self.price=0
        self.value=0

    def Buy(self, price, k):
        self.price = price
        self.fund = self.fund - price * k
        self.stock = self.stock + k
        self.value=self.stock * self.price + self.fund
        print("buy",price,k)
        self.ViewPosition()


    def Sell(self, price, k):
        self.price = price
        self.fund = self.fund + price * k
        self.stock = self.stock-k
        self.value=self.stock * self.price + self.fund
        print("sell", price, k)
        self.ViewPosition()

    def ViewPosition(self):
        print("fund:",self.fund)
        print("stock:",self.stock)
        print("value",self.value)
