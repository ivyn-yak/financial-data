from pydantic import BaseModel
from datetime import date
from typing import Optional
from uuid import UUID
from schemas.enums import Period

# Input schema
class IncomeStatementInput(BaseModel):
    company_id: UUID
    fiscalDateEnding: date
    reportedCurrency: Optional[str]
    period: Period

    grossProfit: Optional[int]
    totalRevenue: Optional[int]
    costOfRevenue: Optional[int]
    operatingIncome: Optional[int]
    operatingExpenses: Optional[int]
    sellingGeneralAndAdministrative: Optional[int]
    researchAndDevelopment: Optional[int]
    depreciationAndAmortization: Optional[int]
    incomeBeforeTax: Optional[int]
    incomeTaxExpense: Optional[int]
    netIncomeFromContinuingOperations: Optional[int]
    ebit: Optional[int]
    ebitda: Optional[int]
    netIncome: Optional[int]

    investmentIncomeNet: Optional[int]
    netInterestIncome: Optional[int]
    interestIncome: Optional[int]
    interestExpense: Optional[int]
    nonInterestIncome: Optional[int]
    otherNonOperatingIncome: Optional[int]
    depreciation: Optional[int]
    interestAndDebtExpense: Optional[int]
    comprehensiveIncomeNetOfTax: Optional[int]

# Output schema
class IncomeStatementSchema(IncomeStatementInput):
    id: UUID

    class Config:
        from_attributes = True
