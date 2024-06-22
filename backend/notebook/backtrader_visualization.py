import backtrader as bt
import datetime
import matplotlib.pyplot as plt
import yfinance as yf

class SimpleStrategy(bt.Strategy):
    def __init__(self):
        self.sma = bt.indicators.SimpleMovingAverage(self.data.close, period=20)

    def next(self):
        if not self.position:
            if self.data.close[0] > self.sma[0]:
                self.buy()
        else:
            if self.data.close[0] < self.sma[0]:
                self.sell()

def run_backtest():
    # Initialize Cerebro
    cerebro = bt.Cerebro()

    # Download data
    df = yf.download('AAPL', start='2020-01-01')

    # Create a data feed
    feed = bt.feeds.PandasData(dataname=df)

    # Add the data feed to Cerebro
    cerebro.adddata(feed)

    # Add our strategy
    cerebro.addstrategy(SimpleStrategy)

    # Set our desired cash start
    cerebro.broker.setcash(10000.0)

    # Add a FixedSize sizer according to the stake
    cerebro.addsizer(bt.sizers.FixedSize, stake=10)

    # Set the commission - 0.1% ... divide by 100 to remove the %
    cerebro.broker.setcommission(commission=0.001)

    # Run the strategy
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
    cerebro.run()
    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

    # Set up the plot
    plt.rcParams['figure.figsize'] = [15, 12]
    plt.rcParams.update({'font.size': 12})

    # Plot the results
    cerebro.plot(iplot=False)
    cerebro.plot(iplot=False, volume=False, style='candlestick')

if __name__ == '__main__':
    run_backtest()