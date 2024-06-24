import React from 'react';

function User_input() {
  return (
    <div className="container mx-auto p-4 pt-6">
      <h1 className="text-3xl font-bold mb-4">Mela</h1>
      <form>
        <div className="flex flex-wrap justify-center mb-4">
          <label className="block text-gray-700 text-sm font-bold mb-2">
            Choose Stocks
          </label>
          <select className="block w-full mt-1 text-sm text-gray-900">
            <option value="AAPL">Apple (AAPL)</option>
            {/* Add more options here */}
          </select>
        </div>
        <div className="flex flex-wrap justify-center mb-4">
          <label className="block text-gray-700 text-sm font-bold mb-2">
            Choose Strategies
          </label>
          <select className="block w-full mt-1 text-sm text-gray-900">
            <option value="SMA">Simple Moving Average (SMA)</option>
            <option value="EMA">Exponential Moving Average (EMA)</option>
            {/* Add more options here */}
          </select>
        </div>
        <div className="flex flex-wrap justify-center mb-4">
          <label className="block text-gray-700 text-sm font-bold mb-2">
            Start Date
          </label>
          <input
            type="date"
            className="block w-full mt-1 text-sm text-gray-900"
            placeholder="Start Date"
          />
        </div>
        <div className="flex flex-wrap justify-center mb-4">
          <label className="block text-gray-700 text-sm font-bold mb-2">
            End Date
          </label>
          <input
            type="date"
            className="block w-full mt-1 text-sm text-gray-900"
            placeholder="End Date"
          />
        </div>
        <div className="flex flex-wrap justify-center mb-4">
          <label className="block text-gray-700 text-sm font-bold mb-2">
            Initial Cash
          </label>
          <input
            type="number"
            className="block w-full mt-1 text-sm text-gray-900"
            placeholder="Initial Cash"
          />
        </div>
        <button
          type="submit"
          className="bg-orange-500 hover:bg-orange-700 text-white font-bold py-2 px-4 rounded"
        >
          Backtesting
        </button>
      </form>
    </div>
  );
}

export default User_input;