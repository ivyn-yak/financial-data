import requests
from api.utils import save_to_json, build_news_filename
import requests_cache

class AlphaVantage:
    BASE_URL = "https://www.alphavantage.co/query"

    def __init__(self, api_key: str, cache_name="av_cache", expire_after=3600):
        self.session = requests_cache.CachedSession(
            cache_name=cache_name,
            backend="sqlite",
            expire_after=expire_after,
            allowable_methods=("GET", "POST"),
            allowable_codes=(200,),
            stale_if_error=True,
        )
        self.api_key = api_key

    # Can be reused for different functions by changing the 'function' parameter
    # eg. "OVERVIEW", "INCOME_STATEMENT", "BALANCE_SHEET", "CASH_FLOW"
    def get_fundamental_data(self, symbol, function="OVERVIEW"):
        params = {
            "function": function,
            "symbol": symbol,
            "apikey": self.api_key,
        }
        response = self.session.get(self.BASE_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            save_to_json(data, f"{symbol}_{function}.json")
            return data
        else:
            response.raise_for_status()

    def get_news_sentiment(self, tickers, topics, time_from, time_to, sort, limit):
        params = {
            "function": "NEWS_SENTIMENT",
            "apikey": self.api_key,
        }

        if tickers:
            params["tickers"] = ",".join(tickers)
        if topics:
            params["topics"] = ",".join(topics)
        if time_from:
            params["time_from"] = time_from
        if time_to:
            params["time_to"] = time_to
        if sort:
            params["sort"] = sort
        if limit:
            params["limit"] = limit
        
        response = self.session.get(self.BASE_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            news_filename = build_news_filename(tickers, topics, time_from, time_to, sort, limit)
            save_to_json(data, news_filename)
            return data
        else:
            response.raise_for_status()

    def get_earnings_transcript(self, symbol, quarter):
        params = {
            "function": "EARNINGS_CALL_TRANSCRIPT",
            "symbol": symbol,
            "quarter": quarter,
            "apikey": self.api_key,
        }

        response = self.session.get(self.BASE_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            save_to_json(data, f"{symbol}_transcript_q{quarter}.json")
            return data
        else:
            response.raise_for_status()

    def get_quote_endpoint(self, symbol):
        params = {
            "function": "GLOBAL_QUOTE",
            "symbol": symbol,
            "apikey": self.api_key,
        }
        response = self.session.get(self.BASE_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            response.raise_for_status()

    def get_historical_data(self, symbol, outputsize="compact"):
        params = {
            "function": "TIME_SERIES_DAILY",
            "symbol": symbol,
            "outputsize": outputsize,
            "apikey": self.api_key,
        }
        response = self.session.get(self.BASE_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            save_to_json(data, f"{symbol}_historical_daily.json")
            return data
        else:
            response.raise_for_status()
