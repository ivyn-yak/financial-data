from api.yfinance import YFinance
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/api/performance")
    
@router.get("/{symbol}/chart")
def get_performance_graphs(symbol: str, baseline: str = "^GSPC"):
    try:
        yf = YFinance(symbol)
        cum_returns, baseline_cum_returns = yf.get_performance_graphs(baseline_symbol=baseline)
        if cum_returns.empty or baseline_cum_returns.empty:
            raise HTTPException(status_code=404, detail="No historical data available")
    
        return {
            "dates": cum_returns.index.strftime("%Y-%m-%d").tolist(),
            "baseline": {
                "symbol": baseline,
                "cumulative_returns": baseline_cum_returns.tolist()
            },
            "stock": {
                "symbol": symbol,
                "cumulative_returns": cum_returns.tolist()
            },
        }
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
    

