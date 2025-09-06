import uuid
from sqlalchemy import Column, String, Float, Date, BigInteger
from sqlalchemy.dialects.postgresql import UUID
from db import Base

class Company(Base):
    __tablename__ = "company"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    Symbol = Column(String(10), unique=True, index=True, nullable=False)

    # Basic Info
    Name = Column(String(255))
    AssetType = Column(String(50))
    Description = Column(String)  # long text
    Exchange = Column(String(20))
    Currency = Column(String(10))
    Sector = Column(String(100))
    Industry = Column(String(100))
    OfficialSite = Column(String(255))

    # Market Info
    MarketCapitalization = Column(BigInteger)
    PERatio = Column(Float)
    ForwardPE = Column(Float)
    PriceToBookRatio = Column(Float)
    Beta = Column(Float)
    _52WeekHigh = Column(Float)
    _52WeekLow = Column(Float)
    _50DayMovingAverage = Column(Float)
    _200DayMovingAverage = Column(Float)

    # Dividend Info
    DividendPerShare = Column(Float)
    DividendYield = Column(Float)
    DividendDate = Column(Date)
    ExDividendDate = Column(Date)

    # Performance
    EPS = Column(Float)
    ProfitMargin = Column(Float)
    RevenueTTM = Column(BigInteger)
    QuarterlyRevenueGrowthYOY = Column(Float)

    # Analyst Ratings
    AnalystTargetPrice = Column(Float)
    AnalystRatingStrongBuy = Column(Float)
    AnalystRatingBuy = Column(Float)
    AnalystRatingHold = Column(Float)
    AnalystRatingSell = Column(Float)
    AnalystRatingStrongSell = Column(Float)