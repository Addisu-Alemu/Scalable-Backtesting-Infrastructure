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

def get_user_input():
    """
    Get and validate user input for initial cash and date range.
    """
    try:
        # Get and validate initial cash
        initial_cash = float(input("Enter initial cash: "))
        if initial_cash <= 0:
            raise ValueError("Initial cash must be a positive number.")
        
        # Get and validate start and end dates
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")
        
        # Validate date format
        datetime.strptime(start_date, "%Y-%m-%d")
        datetime.strptime(end_date, "%Y-%m-%d")
        
        # Ensure start date is before end date
        if start_date >= end_date:
            raise ValueError("Start date must be before end date.")
        
        return initial_cash, start_date, end_date
    except ValueError as e:
        # Handle input validation errors
        print(f"Error: {e}")
        sys.exit(1)

def run_backtest(initial_cash, start_date, end_date):
    """
    Run the backtest with the given parameters.
    """
    try:
        # Initialize Cerebro engine
        cerebro = bt.Cerebro()
        cerebro.addstrategy(SMA)
        
        # Download data and check if it's available
        df = yf.download('SPY', start=start_date, end=end_date)
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
        
        print(f"Return: {(cerebro.broker.getvalue() / initial_cash - 1) * 100:.2f}%")
        print(f"Number of trades: {trade_analyzer.total.total}")
        print(f"Winning trades: {trade_analyzer.won.total}")
        print(f"Losing trades: {trade_analyzer.lost.total}")
        print(f"Max drawdown: {drawdown:.2f}%")
        
        # Plot the results
        cerebro.plot()
    except Exception as e:
        # Handle any errors that occur during backtesting
        print(f"An error occurred during backtesting: {e}")
        sys.exit(1)

if __name__ == '__main__':
    try:
        # Get user input and run the backtest
        initial_cash, start_date, end_date = get_user_input()
        run_backtest(initial_cash, start_date, end_date)
    except KeyboardInterrupt:
        # Handle user interruption (e.g., Ctrl+C)
        print("\nProgram interrupted by user.")
        sys.exit(0)
    except Exception as e:
        # Handle any unexpected errors
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)