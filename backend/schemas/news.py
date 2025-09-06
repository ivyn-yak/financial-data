from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from uuid import UUID

class TickerSentimentSchema(BaseModel):
    ticker: str
    relevance_score: Optional[float]
    ticker_sentiment_score: Optional[float]
    ticker_sentiment_label: Optional[str]

    class Config:
        from_attributes = True

class NewsTopicSchema(BaseModel):
    topic: str
    relevance_score: Optional[float]

    class Config:
        from_attributes = True

class NewsArticleInput(BaseModel):
    title: str
    url: str
    time_published: datetime
    summary: Optional[str]
    banner_image: Optional[str]
    source: Optional[str]
    category_within_source: Optional[str]
    source_domain: Optional[str]
    overall_sentiment_score: Optional[float]
    overall_sentiment_label: Optional[str]
    ticker_sentiment: List[TickerSentimentSchema] = []
    topic: List[NewsTopicSchema] = []

class NewsArticleSchema(NewsArticleInput):
    id: UUID

    class Config:
        from_attributes = True
