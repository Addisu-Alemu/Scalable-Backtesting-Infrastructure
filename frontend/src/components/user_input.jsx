import React, { useState } from 'react';
import "./user_input.css";

function UserInput() {
  const [formData, setFormData] = useState({
    stock: '',
    strategy: '',
    startDate: '',
    endDate: '',
    initialCash: '',
  });

  const [backtestResult, setBacktestResult] = useState(null); // State for the result

  const handleChange = (event) => {
    setFormData({ ...formData, [event.target.name]: event.target.value });
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    const startDateString = formData.startDate;
    const endDateString = formData.endDate;

    const startDate = new Date(startDateString);
    const endDate = new Date(endDateString);

    const startDateFormat = `${startDate.getFullYear()}-${(`0${startDate.getMonth() + 1}`).slice(-2)}-${(`0${startDate.getDate()}`).slice(-2)}`;
    const endDateFormat = `${endDate.getFullYear()}-${(`0${endDate.getMonth() + 1}`).slice(-2)}-${(`0${endDate.getDate()}`).slice(-2)}`;

    try {
      const response = await fetch('http://localhost:8000/backtesting', { 
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          stock: formData.stock,
          strategy: formData.strategy,
          start_date: startDateFormat, 
          end_date: endDateFormat, 
          initial_cash: formData.initialCash
        }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      setBacktestResult(data.result); 
    } catch (error) {
      console.error('Error fetching data:', error);
      setBacktestResult(null); // Clear the result on error
      // Handle the error appropriately, e.g., display an error message to the user
    }
  };

  return (
    <>
    <div className='user-page-container'>
  <div className="user-input-container">
  <div className="user-input-wrapper">
    <div className="user-input-title">
      <span>Mela</span>
    </div>
    <form onSubmit={handleSubmit}>
      <div className="user-input-row">
        <select 
          name="stock" 
          value={formData.stock} 
          onChange={handleChange}
        >
          <option value="" disabled hidden>Choose Stocks</option>
          <option value="AAPL">Apple (AAPL)</option>
          <option value="GOOGL">Google (GOOGL)</option>
          <option value="MSFT">Microsoft (MSFT)</option>
          <option value="AMZN">Amazon (AMZN)</option>
          {/* Add more stock options as needed */}
        </select>
      </div>
      <div className="user-input-row">
        <select 
          name="strategy" 
          value={formData.strategy} 
          onChange={handleChange}
        >
          <option value="" disabled hidden>Choose Strategies</option>
          <option value="SMA">Simple Moving Average (SMA)</option>
          <option value="EMA">Exponential Moving Average (EMA)</option>
          <option value="MACD">Moving Average Convergence Divergence (MACD)</option>
          <option value="RSI">Relative Strength Index (RSI)</option>
          {/* Add more strategy options as needed */}
        </select>
      </div>
      <div className="user-input-row">
        <input 
          type="date" 
          name="startDate" 
          placeholder="Start Date"
          value={formData.startDate} 
          onChange={handleChange} 
        />
      </div>
      <div className="user-input-row">
        <input 
          type="date" 
          name="endDate" 
          placeholder="End Date"
          value={formData.endDate} 
          onChange={handleChange} 
        />
      </div>
      <div className="user-input-row">
        <input 
          type="number" 
          name="initialCash" 
          placeholder="Initial Cash"
          value={formData.initialCash} 
          onChange={handleChange} 
        />
      </div>
      <div className="user-input-row user-input-button">
        <input type="submit" value="Backtesting" />
      </div>
    </form>
  </div>
</div>

<div className="backtest-result-container">
  <div className="backtest-metrics-title">
    <span>Backtesting Metrics</span>
  </div>
  <div className="backtest-metrics">
    <div className="metrics-row">
      <label>Return:</label>
      <div className="metrics-field">
        <input type="text" value={backtestResult && backtestResult.return + "%"} readOnly />
      </div>
    </div>
    <div className="metrics-row">
      <label>Num Trades:</label>
      <div className="metrics-field">
        <input type="text" value={backtestResult && backtestResult.num_trades} readOnly />
      </div>
    </div>
    <div className="metrics-row">
      <label>Winning Trades:</label>
      <div className="metrics-field">
        <input type="text" value={backtestResult && backtestResult.winning_trades} readOnly />
      </div>
    </div>
    <div className="metrics-row">
      <label>Losing Trades:</label>
      <div className="metrics-field">
        <input type="text" value={backtestResult && backtestResult.losing_trades} readOnly />
      </div>
    </div>
    <div className="metrics-row">
      <label>Max Drawdown:</label>
      <div className="metrics-field">
        <input type="text" value={backtestResult && backtestResult.max_drawdown + "%"} readOnly />
      </div>
    </div>
  </div>
</div>  
</div>
</>
  );
}

export default UserInput;