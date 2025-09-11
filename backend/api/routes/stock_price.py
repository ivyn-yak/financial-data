from api.alphavantage import AlphaVantage
from api.yfinance import YFinance
from fastapi import APIRouter, HTTPException
import os
from dotenv import load_dotenv

router = APIRouter(prefix="/api/stock-price")

load_dotenv()
ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")

@router.get("/{symbol}")
def get_stock_price(symbol: str):
    av = AlphaVantage(ALPHA_VANTAGE_API_KEY)
    try:
        response = av.get_quote_endpoint(symbol)
        print(response)
        quote = response.get("Global Quote", {})
        if not quote:
            raise HTTPException(status_code=404, detail="Symbol not found")
        return {
            "symbol": quote["01. symbol"],
            "open": float(quote["02. open"]),
            "high": float(quote["03. high"]),
            "low": float(quote["04. low"]),
            "last_price": float(quote["05. price"]),
            "volume": int(quote["06. volume"]),
            "latest_trading_day": quote["07. latest trading day"],
            "previous_close": float(quote["08. previous close"]),
            "change": float(quote["09. change"]),
            "percent_change": float(quote["10. change percent"].replace("%", "")),
        }
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.get("/{symbol}/history")
def get_stock_history(symbol: str):
    av = AlphaVantage(ALPHA_VANTAGE_API_KEY)
    try:
        stock_chart = av.get_historical_data(symbol)
        if not stock_chart:
            raise HTTPException(status_code=404, detail="No historical data available")
        return stock_chart
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/yf/{symbol}/history")
def get_stock_history_yf(symbol: str):
    try:
        yf = YFinance(symbol)
        stock_chart = yf.get_stock_price()
        if stock_chart.empty:
            raise HTTPException(status_code=404, detail="No historical data available")
        return  [
            {
                "x": date, 
                "o": row["Open"],
                "h": row["High"],
                "l": row["Low"],
                "c": row["Close"]
            }
            for date, row in stock_chart.iterrows()
        ]
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/yf/{symbol}")
def get_stock_price(symbol: str):
    try:
        yf = YFinance(symbol)
        quote = yf.get_fast_info()
        if not quote:
            raise HTTPException(status_code=404, detail="Symbol not found")
        last_price = float(quote.get("lastPrice", 0))
        previous_close = float(quote.get("previousClose", 0))

        change = last_price - previous_close
        percent_change = (change / previous_close) * 100
        return {
            "symbol": symbol,
            "open": float(quote.get("open", 0)),
            "high": float(quote.get("dayHigh", 0)),
            "low": float(quote.get("dayLow", 0)),
            "volume": int(quote.get("lastVolume", 0)),
            "year_high": float(quote.get("yearHigh", 0)),
            "year_low": float(quote.get("yearLow", 0)),
            "market_cap": float(quote.get("marketCap", 0)),
            "currency": quote.get("currency", "USD"),
            "change": change,
            "percent_change": percent_change,
            "last_price": last_price,
        }
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))