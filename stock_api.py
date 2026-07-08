"""
fastapi-stock-api

Simple REST API using FastAPI with simulated stock market data.

Author: Verdiér
License: MIT
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="FastAPI Stock API",
    description="Simple stock API with simulated market data.",
    version="1.0.0",
)


class Stock(BaseModel):
    ticker: str
    company: str
    price: float
    change: float


stocks = {
    "AAPL": Stock(
        ticker="AAPL",
        company="Apple",
        price=212.45,
        change=1.25,
    ),
    "MSFT": Stock(
        ticker="MSFT",
        company="Microsoft",
        price=518.70,
        change=-0.82,
    ),
    "NVDA": Stock(
        ticker="NVDA",
        company="NVIDIA",
        price=174.30,
        change=2.91,
    ),
}


@app.get("/")
def root():
    return {
        "message": "FastAPI Stock API"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/stocks")
def get_stocks():
    return list(stocks.values())


@app.get("/stocks/{ticker}")
def get_stock(ticker: str):

    ticker = ticker.upper()

    if ticker not in stocks:
        raise HTTPException(
            status_code=404,
            detail="Ticker not found."
        )

    return stocks[ticker]


@app.get("/metrics")
def metrics():

    prices = [stock.price for stock in stocks.values()]

    return {
        "stocks": len(stocks),
        "average_price": round(sum(prices) / len(prices), 2),
        "highest_price": max(prices),
        "lowest_price": min(prices),
    }
