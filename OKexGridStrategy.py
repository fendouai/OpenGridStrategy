import os
import numpy as np
import pandas as pd
from GridStrategy import GridStrategy
from Position import Position

# 画格子
grid_num = 100
fund_init = 10000
p = Position(fund_init)
# 固定额度，利润不重新投入，固定每一份投资额。
grid_fund = fund_init / grid_num
f = "Okcoin_BTCUSD_d.csv"
df = pd.read_csv(os.path.join("okcoin", f), header=1)
print(df)

avg = np.mean(df["Close"])
min = np.min(df["Close"])
max = np.max(df["Close"])
print(avg, min, max)
# 网格参数初始化
grid_strategy = GridStrategy(grid_num, min, max)
# 不需要保存状态，只需要保持对称就可以了，记个数字，表明成交对数。
# 增加了持仓，同时增加需要卖的卖单；卖出增加，就增加买单，对应的。
# 已经买的单为0，需要卖的单为0，可以买的单就是  grid_num/2
buy_num = 0


# 如果价格低于中间价格，准备买入
# 如果价格高于中间价格，准备卖出

def grid_trade(price, p, grid_strategy, buy_num):
    # 先算格子
    if price < grid_strategy.middle_price:
        low_grid_num = (grid_strategy.middle_price - price) // grid_strategy.len
        # 跌破，数量是0也是可以的，说明跌破了最低价。
        # 判断当前格子线，成交状态
        if (low_grid_num > buy_num):
            p.Buy(price, grid_fund / price)
            # 买单 +1
            buy_num += 1
        else:
            print("the buy order is done!")

    elif price > grid_strategy.middle_price and buy_num > 0:
        # high_grid_num=(grid_strategy.high-price)//grid_strategy.len
        # 2 1 0 递减
        # 买单的数量是 3 2 1递减
        high_grid_num = (grid_strategy.high - price) // grid_strategy.len + 1
        # 当前格子要是未成交状态
        if (high_grid_num > buy_num):
            # 判断当前格子线，成交状态
            p.Sell(price, grid_fund / price)
            # 买单 +1
            buy_num -= 1
        else:
            print("the sell order is done!")

    return buy_num


for i in range(2200, -1, -1):
    price = df["Close"][i]
    print(price)
    buy_num = grid_trade(price, p, grid_strategy, buy_num)
