import uuid
from sqlalchemy import Column, BigInteger, Date, String, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID
from db import Base
from schemas.enums import Period

class CashFlowStatement(Base):
    __tablename__ = "cash_flow_statement"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    company_id = Column(UUID(as_uuid=True), ForeignKey("company.id"), nullable=False)

    fiscalDateEnding = Column(Date)
    reportedCurrency = Column(String(10))
    period = Column(Enum(Period), nullable=False)

    # Operating Cash Flow
    operatingCashflow = Column(BigInteger, nullable=True)
    paymentsForOperatingActivities = Column(BigInteger, nullable=True)
    proceedsFromOperatingActivities = Column(BigInteger, nullable=True)
    changeInOperatingLiabilities = Column(BigInteger, nullable=True)
    changeInOperatingAssets = Column(BigInteger, nullable=True)
    depreciationDepletionAndAmortization = Column(BigInteger, nullable=True)
    capitalExpenditures = Column(BigInteger, nullable=True)
    changeInReceivables = Column(BigInteger, nullable=True)
    changeInInventory = Column(BigInteger, nullable=True)
    profitLoss = Column(BigInteger, nullable=True)

    # Investing Cash Flow
    cashflowFromInvestment = Column(BigInteger, nullable=True)

    # Financing Cash Flow
    cashflowFromFinancing = Column(BigInteger, nullable=True)
    proceedsFromRepaymentsOfShortTermDebt = Column(BigInteger, nullable=True)
    paymentsForRepurchaseOfCommonStock = Column(BigInteger, nullable=True)
    paymentsForRepurchaseOfEquity = Column(BigInteger, nullable=True)
    paymentsForRepurchaseOfPreferredStock = Column(BigInteger, nullable=True)
    dividendPayout = Column(BigInteger, nullable=True)
    dividendPayoutCommonStock = Column(BigInteger, nullable=True)
    dividendPayoutPreferredStock = Column(BigInteger, nullable=True)
    proceedsFromIssuanceOfCommonStock = Column(BigInteger, nullable=True)
    proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet = Column(BigInteger, nullable=True)
    proceedsFromIssuanceOfPreferredStock = Column(BigInteger, nullable=True)
    proceedsFromRepurchaseOfEquity = Column(BigInteger, nullable=True)
    proceedsFromSaleOfTreasuryStock = Column(BigInteger, nullable=True)
    changeInCashAndCashEquivalents = Column(BigInteger, nullable=True)
    changeInExchangeRate = Column(BigInteger, nullable=True)

    netIncome = Column(BigInteger, nullable=True)
