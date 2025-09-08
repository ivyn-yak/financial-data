from api.alphavantage import AlphaVantage
from fastapi import APIRouter, HTTPException
import os
from dotenv import load_dotenv

router = APIRouter(prefix="/stock-price")

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
