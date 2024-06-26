# Scalable-Backtesting-Infrastructure

## Business Need

Mela, an innovative startup, aims to democratize access to the cryptocurrency market while providing investors with a reliable investment source and mitigating the risks associated with crypto trading. This project focuses on designing and building a robust, scalable trading data pipeline.

## Backtesting

Backtesting is a crucial process in trading strategy development. It involves evaluating the performance of a trading strategy or investment model by applying it to historical market data. This simulation helps in understanding how the strategy would have performed in past market conditions.

## Methodology

### 1. Setup and Installation

- Install Backtrader: `pip install backtrader`
- Install additional dependencies: `pip install -r requirements.txt`

### 2. Data Preparation

- Collect historical data (CSV, pandas DataFrame, or other supported formats)
- Ensure data includes OHLCV (Open, High, Low, Close, Volume) information

### 3. Define Strategy

- Create a class that inherits from `backtrader.Strategy`
- Implement `__init__`, `next`, and optionally `start`, `stop` methods
- Define indicators, entry/exit rules, and position sizing

### 4. Set up the Cerebro engine

- Create a Cerebro instance
- Add data feeds
- Add the strategy
- Set starting cash
- Add analyzers and observers

### 5. Run the backtest

- Call `cerebro.run()`

### 6. Analyze results

- Examine performance metrics
- Visualize results using `cerebro.plot()`

## Running the Project

### Frontend

`cd front_end`
`npm install`
`npm run dev`

### Backtesting

`python3 user_input.py`

### Model Training

`cd Model`

`python3 lstm_model.py`

`MLflow Integration`

python3 mlflow_for_model.py
### Backend (FastAPI)

`cd backend/scripts`

`fastapi dev main.py`

### Requirements
All project dependencies are listed in requirements.txt. Install them using:


`pip install -r requirements.txt`

This project combines advanced trading strategies with machine learning models and provides a user-friendly interface for strategy backtesting and analysis. It leverages popular tools like Backtrader for strategy implementation, LSTM for predictive modeling, and MLflow for experiment tracking.