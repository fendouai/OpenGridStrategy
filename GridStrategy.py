

class GridStrategy(object):
    def __init__(self,num,low,high):
        self.num =num
        self.low =low
        self.high =high
        self.middle_price=(low+high)/2
        self.len=(high-low)/num
