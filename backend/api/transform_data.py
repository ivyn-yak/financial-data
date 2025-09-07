from api.utils import filter_json_for_model
from schemas import *
from typing import List
from models import Company
from db import SessionLocal

class TransformData:
    def __init__(self):
        pass

    def get_session(self):
        return SessionLocal()
    
    def get_company_id(self, symbol):
        session = self.get_session()
        company = session.query(Company).filter(Company.Symbol == symbol).first()
        session.close()
        if company:
            return company.id
        return None

    def get_company_schema(self, json_data) -> CompanyInput:
        filtered_data = filter_json_for_model(json_data, CompanyInput)
        return CompanyInput(**filtered_data)
    
    def get_financials_schema(self, json_data, model, quarters=4):
        symbol = json_data.get("symbol", "")
        quarterly_reports = json_data.get("quarterlyReports", [])
        annual_reports = json_data.get("annualReports", [])

        filtered_quarterly_reports = self._filter_quarterly_reports(symbol, quarterly_reports, model, quarters, period="Quarterly")
        filtered_annual_reports = self._filter_quarterly_reports(symbol, annual_reports, model, quarters, period="Annual")

        merged = filtered_quarterly_reports + filtered_annual_reports
        merged.sort(key=lambda x: x.fiscalDateEnding, reverse=True)

        return merged
    
    def get_news_articles_schema(self, json_data) -> List[NewsArticleInput]:
        articles = json_data.get("feed", [])
        article_schemas = []

        for article in articles:
            news_topics_arr = self._get_news_topics(article.get("topics", []))
            ticker_sentiments_arr = self._get_ticker_sentiment(article.get("ticker_sentiments", []))
        
            filtered_data = filter_json_for_model(article, NewsArticleInput)
            filtered_data["topics"] = news_topics_arr
            filtered_data["ticker_sentiments"] = ticker_sentiments_arr
            article_schemas.append(NewsArticleInput(**filtered_data))
    
        return article_schemas
    
    def get_earnings_call_schema(self, json_data) -> EarningsCallInput:
        symbol = json_data.get("symbol", "")
        company_id = self.get_company_id(symbol)
        if company_id is None:
            raise ValueError(f"Company with symbol {symbol} not found.")
        
        transcipt = json_data.get("transcript", [])
        transcript_segments_arr = self._get_transcript_segments(transcipt)

        filtered_data = filter_json_for_model(json_data, EarningsCallBase)
        filtered_data["transcript_segment"] = transcript_segments_arr
        filtered_data["company_id"] = company_id

        return EarningsCallInput(**filtered_data)

    def _filter_quarterly_reports(self, symbol, reports, model, quarters=8, period="Quarterly"):
        company_id = self.get_company_id(symbol)
        if company_id is None:
            raise ValueError(f"Company with symbol {symbol} not found.")
        
        filtered_data_list = []
        for report in reports[:quarters]:
            filtered_data = filter_json_for_model(report, model)
            filtered_data["company_id"] = company_id
            filtered_data["period"] = period
            filtered_data_list.append(model(**filtered_data))
            
        return filtered_data_list
    
    def _get_news_topics(self, news_topics):
        arr = []
        for topic in news_topics:
            filtered_data = filter_json_for_model(topic, NewsTopicSchema)
            arr.append(NewsTopicSchema(**filtered_data))
        return arr
    
    def _get_ticker_sentiment(self, ticker_sentiments):
        arr = []
        for ticker in ticker_sentiments:
            filtered_data = filter_json_for_model(ticker, TickerSentimentSchema)
            arr.append(TickerSentimentSchema(**filtered_data))
        return arr

    def _get_transcript_segments(self, transcipt):
        arr = []
        for segment in transcipt:
            filtered_data = filter_json_for_model(segment, TranscriptSegmentBase)
            arr.append(TranscriptSegmentInput(**filtered_data))
        return arr