from pydantic import BaseModel
from typing import Optional
from datetime import date
from uuid import UUID

# Input schema
class CompanyInput(BaseModel):
    Symbol: str
    Name: Optional[str]
    AssetType: Optional[str]
    Description: Optional[str]
    Exchange: Optional[str]
    Currency: Optional[str]
    Sector: Optional[str]
    Industry: Optional[str]
    OfficialSite: Optional[str]

    MarketCapitalization: Optional[int]
    PERatio: Optional[float]
    ForwardPE: Optional[float]
    PriceToBookRatio: Optional[float]
    Beta: Optional[float]
    _52WeekHigh: Optional[float]
    _52WeekLow: Optional[float]
    _50DayMovingAverage: Optional[float]
    _200DayMovingAverage: Optional[float]

    DividendPerShare: Optional[float]
    DividendYield: Optional[float]
    DividendDate: Optional[date]
    ExDividendDate: Optional[date]

    EPS: Optional[float]
    ProfitMargin: Optional[float]
    RevenueTTM: Optional[int]
    QuarterlyRevenueGrowthYOY: Optional[float]

    AnalystTargetPrice: Optional[float]
    AnalystRatingStrongBuy: Optional[float]
    AnalystRatingBuy: Optional[float]
    AnalystRatingHold: Optional[float]
    AnalystRatingSell: Optional[float]
    AnalystRatingStrongSell: Optional[float]

# Output schema
class CompanySchema(CompanyInput):
    id: UUID

    class Config:
        from_attributes = True
