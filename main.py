
import random as rd
import math
import numpy as np

from utils.indicators import movingAverage
from utils.candle import Candle
from utils.history import History

DURATION = 1 * 24 * 60 # In minutes
INIT_PRICE = 100
rules = [{
    "condition": lambda history: history.candles[-1].close > INIT_PRICE,
    "action": lambda history: history.candles[-1].edit(
        close = history.candles[-1].close + rd.normalvariate(-0.001, 0.5),
    )
},
{
    "condition": lambda history: history.candles[-1].close < INIT_PRICE,
    "action": lambda history: history.candles[-1].edit(
        close = history.candles[-1].close + rd.normalvariate(0.001, 0.5),
    )
},
{
    "condition": lambda history: history.candles[-1].close == INIT_PRICE,
    "action": lambda history: history.candles[-1].edit(
        close = history.candles[-1].close + rd.normalvariate(0, 0.5),
    )
},
{
    "condition": lambda history: history.candles[-1].close / INIT_PRICE < 0.5,
    "action": lambda history: history.candles[-1].edit(
        close = history.candles[-1].close + rd.normalvariate(1 - history.candles[-1].close / INIT_PRICE, 0.5),
    )
},
{
    "condition": lambda history: history.length > 1,
    "action": lambda history: history.candles[-1].edit(
        open = history.candles[-2].close,
        low = min(history.candles[-1].open, history.candles[-1].close) + rd.uniform(-0.4, -0),
        high = max(history.candles[-1].open, history.candles[-1].close) + rd.uniform(0, 0.4),
    )
}]


def main():
    
    # Generate a random history
    history = History()
    history.generateHistory(
        INIT_PRICE, 
        DURATION,
        rules
    )
    history.display([
        lambda history: movingAverage([candle.close for candle in history.candles], 60*24*15)
    ])

if __name__ == '__main__':
    main()