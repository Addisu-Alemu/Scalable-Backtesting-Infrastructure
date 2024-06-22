import backtrader as bt
import datetime
import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd

# Download the data
df = yf.download('AAPL', start='2020-01-01')
df.reset_index(inplace=True)

# Define the class for each strategy
class SmaCross(bt.Strategy):
    """
    This class implements the Simple Moving Average (SMA) strategy.
    """
    def __init__(self):
        self.sma1 = bt.ind.SMA(period=50)  
        self.sma2 = bt.ind.SMA(period=100)  
        self.crossover = bt.ind.CrossOver(self.sma1, self.sma2)  

    def next(self):
        if not self.position:  
            if self.crossover > 0:  
                self.buy()  

        elif self.crossover < 0:  
            self.close()  

class SMA(bt.Strategy):
    """
    This class implements the Simple Moving Average (SMA) strategy.
    """
    params = (
        (' period', 20),  
    )

    def __init__(self):
        self.sma = bt.indicators.SimpleMovingAverage(
            self.data.close,
            period=self.params.period
        )

    def next(self):
        if not self.position:  
            if self.data.close[0] > self.sma[0]:
                self.buy()
        else:  
            if self.data.close[0] < self.sma[0]:
                self.sell()

class EMA(bt.Strategy):
    """
    This class implements the Exponential Moving Average (EMA) strategy.
    """
    params = (
        (' period', 20),  
    )

    def __init__(self):
        self.ema = bt.indicators.ExponentialMovingAverage(
            self.data.close,
            period=self.params.period
        )

    def next(self):
        if not self.position:  
            if self.data.close[0] > self.ema[0]:
                self.buy()
        else:  
            if self.data.close[0] < self.ema[0]:
                self.sell()

class RSIStrategy(bt.Strategy):
    """
    This class implements the Relative Strength Index (RSI) strategy.
    """
    params = (
        (' period', 14),  
        (' overbought', 70),  
        (' oversold', 30),  
    )

    def __init__(self):
        self.rsi = bt.indicators.RSI(
            self.data.close,
            period=self.params.period
        )

    def next(self):
        if not self.position:  
            if self.rsi[0] < self.params.oversold:
                self.buy()
        else:  
            if self.rsi[0] > self.params.overbought:
                self.sell()

class MACDStrategy(bt.Strategy):
    """
    This class implements the Moving Average Convergence Divergence (MACD) strategy.
    """
    params = (
        (' fast_period', 12),  
        (' slow_period', 26),  
        (' signal_period', 9),  
    )

    def __init__(self):
        self.macd = bt.indicators.MACD(
            self.data.close,
            period_me1=self.params.fast_period,
            period_me2=self.params.slow_period,
            period_signal=self.params.signal_period
        )
        self.order = None
        self.trades = 0
        self.winning_trades = 0
        self.losing_trades = 0

    def next(self):
        if not self.position:
            if self.macd.macd[0] > self.macd.signal[0] and self.macd.macd[-1] <= self.macd.signal[-1]:
                self.order = self.buy()
                self.trades += 1
        else:
            if self.macd.macd[0] < self.macd.signal[0] and self.macd.macd[-1] >= self.macd.signal[-1]:
                self.order = self.sell()
                self.trades += 1

    def notify_trade(self, trade):
        if trade.isclosed:
            if trade.pnl > 0:
                self.winning_trades += 1
            else:
                self.losing_trades += 1

# Create the cerebro engine
cerebro = bt.Cerebro()

# Add the data to the cerebro engine
data = yf.download('AAPL', start='2020-01-01')
data.reset_index(inplace=True)
feed = bt.feeds.PandasData(dataname=data)
cerebro.adddata(feed)

# Add the strategies
cerebro.addstrategy(SmaCross)
cerebro.addstrategy(SMA)
cerebro.addstrategy(EMA)
cerebro.addstrategy(RSIStrategy)
cerebro.addstrategy(MACDStrategy)