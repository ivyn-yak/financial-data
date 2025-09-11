from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import desc
from db import get_db
from models import NewsArticle, TickerSentiment
from schemas.news import NewsArticleSchema
from typing import List

router = APIRouter(prefix="/api/news")

@router.get("/", response_model=List[NewsArticleSchema])
def get_all_news(db: Session = Depends(get_db)):
    return db.query(NewsArticle).all()

@router.get("/{symbol}", response_model=List[NewsArticleSchema])
def get_news_by_ticker(symbol: str, db: Session = Depends(get_db)):
    news_list = (
        db.query(NewsArticle)
        .options(
            joinedload(NewsArticle.ticker_sentiment), 
            joinedload(NewsArticle.topic)            
        )
        .join(TickerSentiment)
        .filter(TickerSentiment.ticker == symbol)
        .all()
    )
    return news_list

@router.get("/recent/{symbol}", response_model=List[NewsArticleSchema])
def get_recent_news_by_ticker(symbol: str, db: Session = Depends(get_db), limit: int = 10):
    news_list = (
        db.query(NewsArticle)
        .join(TickerSentiment)
        .filter(TickerSentiment.ticker == symbol)
        .order_by(desc(NewsArticle.time_published))
        .limit(limit)
        .all()
    )
    return news_list