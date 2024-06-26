import backtrader as bt
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import torch
import torch.nn as nn

# LSTM Model
class LSTMModel(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim, num_layers):
        super(LSTMModel, self).__init__()
        self.hidden_dim = hidden_dim
        self.num_layers = num_layers
        self.lstm = nn.LSTM(input_dim, hidden_dim, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_dim).to(x.device)
        c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_dim).to(x.device)
        out, _ = self.lstm(x, (h0, c0))
        out = self.fc(out[:, -1, :])
        return out
# Custom indicator using LSTM
class LSTMIndicator(bt.Indicator):
    lines = ('prediction',)
    params = (('period', 10),)

    def __init__(self):
        self.model = LSTMModel(input_dim=1, hidden_dim=50, output_dim=1, num_layers=1)
        self.model.load_state_dict(torch.load('lstm_model.pth'))
        self.model.eval()
        self.addminperiod(self.params.period)

    def next(self):
        if len(self) >= self.params.period:
            data = np.array([self.data.close.get(size=self.params.period)])
            data = data.reshape(-1, self.params.period, 1)
            data = torch.FloatTensor(data)
            with torch.no_grad():
                prediction = self.model(data)
            self.lines.prediction[0] = prediction.item()

# Strategy
class LSTMStrategy(bt.Strategy):
    params = (('period', 10),)

    def __init__(self):
        self.lstm = LSTMIndicator(period=self.params.period)
        self.sma = bt.indicators.SimpleMovingAverage(period=self.params.period)

    def next(self):
        if not self.position:
            if self.lstm.prediction > self.data.close[0] and self.data.close[0] > self.sma[0]:
                self.buy()
        else:
            if self.lstm.prediction < self.data.close[0] or self.data.close[0] < self.sma[0]:
                self.sell()

# Load and preprocess data
data = pd.read_csv('/home/addisu-alemu/Desktop/week nine/Scalable-Backtesting-Infrastructure/Model/apple_stock.csv', index_col='Date', parse_dates=True)
scaler = MinMaxScaler()
data['Close'] = scaler.fit_transform(data[['Close']])

# Create and train LSTM model (this part would typically be done separately)
X = []
y = []
for i in range(len(data) - 10):
    X.append(data['Close'].values[i:i+10])
    y.append(data['Close'].values[i+10])

X = np.array(X).reshape(-1, 10, 1)
y = np.array(y)

X = torch.FloatTensor(X)
y = torch.FloatTensor(y).view(-1, 1)

model = LSTMModel(input_dim=1, hidden_dim=50, output_dim=1, num_layers=1)
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

for epoch in range(100):
    outputs = model(X)
    optimizer.zero_grad()
    loss = criterion(outputs, y)
    loss.backward()
    optimizer.step()

# Save the trained model
torch.save(model.state_dict(), 'lstm_model.pth')

# Backtrader setup
cerebro = bt.Cerebro()

# Add data feed
data_feed = bt.feeds.PandasData(dataname=data)
cerebro.adddata(data_feed)

# Add strategy
cerebro.addstrategy(LSTMStrategy)

# Set initial cash
cerebro.broker.setcash(100000.0)

# Add commission
cerebro.broker.setcommission(commission=0.001)

# Print starting conditions
print(f'Starting Portfolio Value: {cerebro.broker.getvalue():.2f}')

# Run backtest
results = cerebro.run()

# Print final results
print(f'Final Portfolio Value: {cerebro.broker.getvalue():.2f}')

# Plot the results
cerebro.plot()