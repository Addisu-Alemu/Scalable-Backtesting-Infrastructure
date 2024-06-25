from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts.sma_strategy import run_backtest
from fastapi.middleware.cors import CORSMiddleware # Import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for testing, replace with your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class BacktestingInput(BaseModel):
    stock: str
    strategy: str
    start_date: str
    end_date: str
    initial_cash: int

@app.post("/backtesting")
async def backtesting(input: BacktestingInput):
    try:
        result = run_backtest(input.initial_cash, input.start_date, input.end_date)
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))