import uuid
from sqlalchemy import Column, String, DateTime, Float, ForeignKey, Table
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from db import Base

class NewsArticle(Base):
    __tablename__ = "news_article"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    title = Column(String, nullable=False)
    url = Column(String, nullable=False)
    time_published = Column(DateTime, nullable=False)
    summary = Column(String, nullable=True)
    banner_image = Column(String, nullable=True)
    source = Column(String, nullable=True)
    category_within_source = Column(String, nullable=True)
    source_domain = Column(String, nullable=True)
    overall_sentiment_score = Column(Float, nullable=True)
    overall_sentiment_label = Column(String, nullable=True)

    # One-to-many relationship to ticker sentiments
    ticker_sentiment = relationship("TickerSentiment", back_populates="news_article", cascade="all, delete-orphan")
    topic = relationship("NewsTopic", back_populates="news_article", cascade="all, delete-orphan")

class TickerSentiment(Base):
    __tablename__ = "ticker_sentiment"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    news_article_id = Column(UUID(as_uuid=True), ForeignKey("news_article.id"), nullable=False)
    ticker = Column(String(20), nullable=False)
    relevance_score = Column(Float, nullable=True)
    ticker_sentiment_score = Column(Float, nullable=True)
    ticker_sentiment_label = Column(String, nullable=True)

    news_article = relationship("NewsArticle", back_populates="ticker_sentiment")

class NewsTopic(Base):
    __tablename__ = "news_topic"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    news_article_id = Column(UUID(as_uuid=True), ForeignKey("news_article.id"), nullable=False)
    topic = Column(String, nullable=False)
    relevance_score = Column(Float, nullable=True)

    news_article = relationship("NewsArticle", back_populates="topic")
