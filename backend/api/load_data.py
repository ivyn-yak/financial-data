from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models import *
from schemas import *
from typing import List

class LoadData:
    def __init__(self):
        pass

    def insert_company(self, session: Session, company_schema: CompanyInput):
        """Insert or update a company"""
        try:
            obj = Company(**company_schema.dict())
            session.add(obj)
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()  # rollback everything on error
            print("Error inserting news batch:", e)
            raise
    
    def batch_insert_balance_sheet(self, session: Session, balance_sheets: List[BalanceSheetInput]):
        try:           
            for b in balance_sheets:
                obj = BalanceSheet(**b.dict())
                session.add(obj)
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()  # rollback everything on error
            print("Error inserting news batch:", e)
            raise
    
    def batch_insert_income_statement(self, session: Session, income_statements: List[IncomeStatementInput]):
        try:
            for i in income_statements:
                obj = IncomeStatement(**i.dict())
                session.add(obj)
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()  # rollback everything on error
            print("Error inserting news batch:", e)
            raise

    def batch_insert_cash_flow(self, session: Session, cash_flow: List[CashFlowStatementInput]):
        try:
            for c in cash_flow:
                obj = CashFlowStatement(**c.dict())
                session.add(obj)
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()  # rollback everything on error
            print("Error inserting news batch:", e)
            raise       

    def batch_insert_news(self, session: Session, articles: List[NewsArticleInput]):
        try:
            for article in articles:
                # Convert main article
                news_obj = NewsArticle(
                    title=article.title,
                    url=article.url,
                    time_published=article.time_published,
                    summary=article.summary,
                    banner_image=article.banner_image,
                    source=article.source,
                    category_within_source=article.category_within_source,
                    source_domain=article.source_domain,
                    overall_sentiment_score=article.overall_sentiment_score,
                    overall_sentiment_label=article.overall_sentiment_label
                )
                session.add(news_obj)
                session.flush()  # get the id for FK

                # Insert topics
                for topic in article.topic:
                    topic_obj = NewsTopic(
                        news_article_id=news_obj.id,
                        topic=topic.topic,
                        relevance_score=topic.relevance_score
                    )
                    session.add(topic_obj)

                # Insert ticker sentiments
                for ticker in article.ticker_sentiment:
                    ticker_obj = TickerSentiment(
                        news_article_id=news_obj.id,
                        ticker=ticker.ticker,
                        relevance_score=ticker.relevance_score,
                        ticker_sentiment_score=ticker.ticker_sentiment_score,
                        ticker_sentiment_label=ticker.ticker_sentiment_label
                    )
                    session.add(ticker_obj)

            session.commit()  # commit only if all inserts succeed
        
        except SQLAlchemyError as e:
            session.rollback()  # rollback everything on error
            print("Error inserting news batch:", e)
            raise

    def batch_insert_earnings_transcript(self, session: Session, earnings_call: EarningsCallInput):
        try:
            earnings_obj = EarningsCall(
                company_id=earnings_call.company_id,
                quarter=earnings_call.quarter
            )
            session.add(earnings_obj)
            session.flush()

            # Insert transcript segments
            for transcript in earnings_call.transcript_segment:
                transcript_obj = TranscriptSegment(
                    earnings_call_id=earnings_obj.id,
                    speaker=transcript.speaker,
                    title=transcript.title,
                    content=transcript.content,
                    sentiment=transcript.sentiment
                )
                session.add(transcript_obj)

            session.commit()  # commit only if all inserts succeed
    
        except SQLAlchemyError as e:
            session.rollback()  # rollback everything on error
            print("Error inserting news batch:", e)
            raise
