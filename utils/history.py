
import matplotlib.pyplot as plt
import random as rd

from utils.candle import Candle

class History:
    def __init__ (self, candles: list = []):
        self.candles = candles

    def display(self):
        plt.plot([candle.close for candle in self.candles])
        plt.show()

    def generateHistory(self, initPrice: float = 100, duration: int = 24*60, rules: list = []):
        """
        initPrice: float
        duration: int (in minutes)
        rules: list of objects
          Each object contains a condition (as lambda function) and an action (as lambda function)
          The condition is a function that takes history as argument and returns a boolean
          The action is a function that takes history as argument and modifies it
        """

        # Generate the first candle
        self.candles.append(Candle(initPrice, initPrice, initPrice, initPrice, 0))

        # Generate the following candles
        for i in range(1, duration):
            # Get the previous candle
            previousCandle = self.candles[i-1]

            # Generate the new candle
            newCandle = Candle(previousCandle.close, previousCandle.close, previousCandle.close, previousCandle.close, 0)

            # Apply the rules
            for rule in rules:
                if rule["condition"](self):
                    rule["action"](self)

            # Add the new candle to the history
            self.candles.append(newCandle)