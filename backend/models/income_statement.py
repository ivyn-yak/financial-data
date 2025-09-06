import uuid
from sqlalchemy import Column, String, BigInteger, Date, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from db import Base

class IncomeStatement(Base):
    __tablename__ = "income_statement"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    company_id = Column(UUID(as_uuid=True), ForeignKey("company.id"), nullable=False)

    fiscalDateEnding = Column(Date)
    reportedCurrency = Column(String(10))

    # Key Income Statement Items
    grossProfit = Column(BigInteger)
    totalRevenue = Column(BigInteger)
    costOfRevenue = Column(BigInteger)
    operatingIncome = Column(BigInteger)
    operatingExpenses = Column(BigInteger)
    sellingGeneralAndAdministrative = Column(BigInteger)
    researchAndDevelopment = Column(BigInteger)
    depreciationAndAmortization = Column(BigInteger)
    incomeBeforeTax = Column(BigInteger)
    incomeTaxExpense = Column(BigInteger)
    netIncomeFromContinuingOperations = Column(BigInteger)
    ebit = Column(BigInteger)
    ebitda = Column(BigInteger)
    netIncome = Column(BigInteger)

    # Optional / can be None
    investmentIncomeNet = Column(BigInteger, nullable=True)
    netInterestIncome = Column(BigInteger, nullable=True)
    interestIncome = Column(BigInteger, nullable=True)
    interestExpense = Column(BigInteger, nullable=True)
    nonInterestIncome = Column(BigInteger, nullable=True)
    otherNonOperatingIncome = Column(BigInteger, nullable=True)
    depreciation = Column(BigInteger, nullable=True)
    interestAndDebtExpense = Column(BigInteger, nullable=True)
    comprehensiveIncomeNetOfTax = Column(BigInteger, nullable=True)