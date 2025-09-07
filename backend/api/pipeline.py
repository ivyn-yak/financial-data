from api.alphavantage import AlphaVantage
from api.transform_data import TransformData
from api.load_data import LoadData
from schemas import BalanceSheetInput, IncomeStatementInput, CashFlowStatementInput
from db import SessionLocal

class DataPipeline:
    def __init__(self, api_key):
        self.av = AlphaVantage(api_key)
        self.transformer = TransformData()
        self.loader = LoadData()

    def get_session(self):
        return SessionLocal()
    
    def run_all_by_symbol(self, symbol):
        self.run_company(symbol)
        self.run_balance_sheet(symbol, quarters=12)
        self.run_income_statement(symbol, quarters=12)
        self.run_cash_flow(symbol, quarters=12)
        self.run_news_sentiment(tickers=[symbol])

    def run_company(self, symbol):
        json_data = self.av.get_fundamental_data(symbol, "OVERVIEW")
        processed_data = self.transformer.get_company_schema(json_data)
        session = self.get_session()
        self.loader.insert_company(session, processed_data)
        session.close()

    def run_balance_sheet(self, symbol, quarters=4):
        json_data = self.av.get_fundamental_data(symbol, "BALANCE_SHEET")
        processed_data = self.transformer.get_financials_schema(json_data, BalanceSheetInput, quarters)
        session = self.get_session()
        self.loader.batch_insert_balance_sheet(session, processed_data)
        session.close()

    def run_income_statement(self, symbol, quarters=4):
        json_data = self.av.get_fundamental_data(symbol, "INCOME_STATEMENT")
        processed_data = self.transformer.get_financials_schema(json_data, IncomeStatementInput, quarters)
        session = self.get_session()
        self.loader.batch_insert_income_statement(session, processed_data)
        session.close()

    def run_cash_flow(self, symbol, quarters=4):
        json_data = self.av.get_fundamental_data(symbol, "CASH_FLOW")
        processed_data = self.transformer.get_financials_schema(json_data, CashFlowStatementInput, quarters)
        session = self.get_session()
        self.loader.batch_insert_cash_flow(session, processed_data)
        session.close()
    
    def run_news_sentiment(self, tickers=None, topics=None, time_from=None, time_to=None, sort=None, limit=None):
        json_data = self.av.get_news_sentiment(tickers, topics, time_from, time_to, sort, limit)
        processed_data = self.transformer.get_news_articles_schema(json_data)
        session = self.get_session()
        self.loader.batch_insert_news(session, processed_data)
        session.close()

    def run_earnings_call(self, symbol, quarter):
        json_data = self.av.get_earnings_transcript(symbol, quarter)
        processed_data = self.transformer.get_earnings_call_schema(json_data)
        session = self.get_session()
        self.loader.batch_insert_earnings_transcript(session, processed_data)
        session.close()


    