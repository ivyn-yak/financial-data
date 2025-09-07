import uuid
from sqlalchemy import Column, String, BigInteger, Date, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID
from db import Base
from schemas.enums import Period

class BalanceSheet(Base):
    __tablename__ = "balance_sheet"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    company_id = Column(UUID(as_uuid=True), ForeignKey("company.id"), nullable=False)

    fiscalDateEnding = Column(Date, nullable=False)
    reportedCurrency = Column(String(10))
    period = Column(Enum(Period), nullable=False)

    # Assets
    totalAssets = Column(BigInteger)
    totalCurrentAssets = Column(BigInteger)
    cashAndCashEquivalentsAtCarryingValue = Column(BigInteger)
    cashAndShortTermInvestments = Column(BigInteger)
    inventory = Column(BigInteger)
    currentNetReceivables = Column(BigInteger)
    totalNonCurrentAssets = Column(BigInteger)
    propertyPlantEquipment = Column(BigInteger)
    accumulatedDepreciationAmortizationPPE = Column(BigInteger, nullable=True)
    intangibleAssets = Column(BigInteger)
    intangibleAssetsExcludingGoodwill = Column(BigInteger)
    goodwill = Column(BigInteger)
    investments = Column(BigInteger, nullable=True)
    longTermInvestments = Column(BigInteger, nullable=True)
    shortTermInvestments = Column(BigInteger, nullable=True)
    otherCurrentAssets = Column(BigInteger)
    otherNonCurrentAssets = Column(BigInteger, nullable=True)

    # Liabilities
    totalLiabilities = Column(BigInteger)
    totalCurrentLiabilities = Column(BigInteger)
    currentAccountsPayable = Column(BigInteger)
    deferredRevenue = Column(BigInteger, nullable=True)
    currentDebt = Column(BigInteger, nullable=True)
    shortTermDebt = Column(BigInteger, nullable=True)
    totalNonCurrentLiabilities = Column(BigInteger)
    capitalLeaseObligations = Column(BigInteger, nullable=True)
    longTermDebt = Column(BigInteger, nullable=True)
    currentLongTermDebt = Column(BigInteger, nullable=True)
    longTermDebtNoncurrent = Column(BigInteger, nullable=True)
    shortLongTermDebtTotal = Column(BigInteger, nullable=True)
    otherCurrentLiabilities = Column(BigInteger, nullable=True)
    otherNonCurrentLiabilities = Column(BigInteger, nullable=True)

    # Shareholder Equity
    totalShareholderEquity = Column(BigInteger)
    treasuryStock = Column(BigInteger, nullable=True)
    retainedEarnings = Column(BigInteger)
    commonStock = Column(BigInteger)
    commonStockSharesOutstanding = Column(BigInteger)
