import React from 'react';
import "./user_input.css";

function User_input() {
  return (
    <div className="user-input-container">
      <div className="user-input-wrapper">
        <div className="user-input-title">
          <span>Mela</span>
        </div>
        <form>
          <div className="user-input-row">
            <select defaultValue="">
              <option value="" disabled hidden>Choose Stocks</option>
              <option value="AAPL">Apple (AAPL)</option>
              <option value="GOOGL">Google (GOOGL)</option>
              <option value="MSFT">Microsoft (MSFT)</option>
              <option value="AMZN">Amazon (AMZN)</option>
              {/* Add more stock options as needed */}
            </select>
          </div>
          <div className="user-input-row">
            <select defaultValue="">
              <option value="" disabled hidden>Choose Strategies</option>
              <option value="SMA">Simple Moving Average (SMA)</option>
              <option value="EMA">Exponential Moving Average (EMA)</option>
              <option value="MACD">Moving Average Convergence Divergence (MACD)</option>
              <option value="RSI">Relative Strength Index (RSI)</option>
              {/* Add more strategy options as needed */}
            </select>
          </div>
          <div className="user-input-row">
            <input type="date" placeholder="Start Date" />
          </div>
          <div className="user-input-row">
            <input type="date" placeholder="End Date" />
          </div>
          <div className="user-input-row">
            <input type="number" placeholder="Initial Cash" />
          </div>
          <div className="user-input-row user-input-button">
            <input type="submit" value="Backtesting" />
          </div>
        </form>
      </div>
    </div>
  );
}

export default User_input;