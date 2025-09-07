from pydantic import BaseModel
from typing import Optional
from datetime import date
from uuid import UUID
from schemas.enums import Period
    
# Input schema
class BalanceSheetInput(BaseModel):
    company_id: UUID
    fiscalDateEnding: date
    reportedCurrency: Optional[str]
    period: Period

    # Assets
    totalAssets: Optional[int]
    totalCurrentAssets: Optional[int]
    cashAndCashEquivalentsAtCarryingValue: Optional[int]
    cashAndShortTermInvestments: Optional[int]
    inventory: Optional[int]
    currentNetReceivables: Optional[int]
    totalNonCurrentAssets: Optional[int]
    propertyPlantEquipment: Optional[int]
    accumulatedDepreciationAmortizationPPE: Optional[int]
    intangibleAssets: Optional[int]
    intangibleAssetsExcludingGoodwill: Optional[int]
    goodwill: Optional[int]
    investments: Optional[int]
    longTermInvestments: Optional[int]
    shortTermInvestments: Optional[int]
    otherCurrentAssets: Optional[int]
    otherNonCurrentAssets: Optional[int]

    # Liabilities
    totalLiabilities: Optional[int]
    totalCurrentLiabilities: Optional[int]
    currentAccountsPayable: Optional[int]
    deferredRevenue: Optional[int]
    currentDebt: Optional[int]
    shortTermDebt: Optional[int]
    totalNonCurrentLiabilities: Optional[int]
    capitalLeaseObligations: Optional[int]
    longTermDebt: Optional[int]
    currentLongTermDebt: Optional[int]
    longTermDebtNoncurrent: Optional[int]
    shortLongTermDebtTotal: Optional[int]
    otherCurrentLiabilities: Optional[int]
    otherNonCurrentLiabilities: Optional[int]

    # Shareholder Equity
    totalShareholderEquity: Optional[int]
    treasuryStock: Optional[int]
    retainedEarnings: Optional[int]
    commonStock: Optional[int]
    commonStockSharesOutstanding: Optional[int]

# Output schema
class BalanceSheetSchema(BalanceSheetInput):
    id: UUID

    class Config:
        from_attributes = True
