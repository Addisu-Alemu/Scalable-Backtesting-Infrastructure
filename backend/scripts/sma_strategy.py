import backtrader as bt
import yfinance as yf
from datetime import datetime
import sys

class SMA(bt.Strategy):
    params = (
        ('period', 20),  # Default SMA period
    )

    def __init__(self):
        self.sma = bt.indicators.SimpleMovingAverage(
            self.data.close,
            period=self.params.period
        )

    def next(self):
        if not self.position:  # Not in the market
            if self.data.close[0] > self.sma[0]:
                self.buy()
        else:  # In the market
            if self.data.close[0] < self.sma[0]:
                self.sell()

def run_backtest( initial_cash, start_date, end_date):
    """
    Run the backtest with the given parameters.
    """
    try:
        # Initialize Cerebro engine
        cerebro = bt.Cerebro()
        cerebro.addstrategy(SMA)  # Use the selected strategy
        
        # Download data and check if it's available
        df = yf.download("SPY", start=start_date, end=end_date)
        if df.empty:
            raise ValueError("No data available for the specified date range.")
        
        # Add data feed to Cerebro
        data = bt.feeds.PandasData(dataname=df)
        cerebro.adddata(data)
        
        # Set initial cash
        cerebro.broker.set_cash(initial_cash)
        
        # Add analyzers
        cerebro.addanalyzer(bt.analyzers.DrawDown, _name='drawdown')
        cerebro.addanalyzer(bt.analyzers.TradeAnalyzer, _name='tradeanalyzer')
        
        # Run the backtest
        results = cerebro.run()
        strat = results[0]
        
        # Extract and print results
        drawdown = strat.analyzers.drawdown.get_analysis()['max']['drawdown']
        trade_analyzer = strat.analyzers.tradeanalyzer.get_analysis()
        
        result = {
            "return": (cerebro.broker.getvalue() / initial_cash - 1) * 100,
            "num_trades": trade_analyzer.total.total,
            "winning_trades": trade_analyzer.won.total,
            "losing_trades": trade_analyzer.lost.total,
            "max_drawdown": drawdown
        }
        
        return result
    except Exception as e:
        # Handle any errors that occur during backtesting
        return {"error": str(e)}

if __name__ == '__main__':
    # This script will be called from the FastAPI endpoint, so we don't need to get user input here
    pass