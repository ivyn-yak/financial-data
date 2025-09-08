from api.utils import save_to_json, build_news_filename
import requests_cache
import yfinance as yf
import pandas as pd

class YFinance:

    def __init__(self, symbol: str, cache_name="yf_cache", expire_after=3600):
        self.session = requests_cache.CachedSession(
            cache_name=cache_name,
            backend="sqlite",
            expire_after=expire_after,
            allowable_methods=("GET", "POST"),
            allowable_codes=(200,),
            stale_if_error=True,
        )
        self.symbol = symbol
        self.ticker = yf.Ticker(symbol)

    def get_performance_graphs(self, baseline_symbol="^GSPC", period="3mo"):
        # Use S&P 500 as baseline
        baseline = yf.Ticker(baseline_symbol)
        baseline_hist = baseline.history(period=period)['Close']
        baseline_cum_returns = self._get_cumulative_returns(baseline_hist)

        hist = self.ticker.history(period=period)['Close']
        cum_returns = self._get_cumulative_returns(hist)

        return cum_returns, baseline_cum_returns

    def _get_cumulative_returns(self, hist: pd.Series) -> pd.Series:
        daily_returns = hist.pct_change().fillna(0)
        cum_returns = (1 + daily_returns).cumprod() - 1
        return cum_returns


