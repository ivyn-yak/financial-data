from pydantic import BaseModel
from typing import Optional
from datetime import date
from uuid import UUID

# Input schema
class CashFlowStatementInput(BaseModel):
    company_id: UUID
    fiscalDateEnding: date
    reportedCurrency: Optional[str]

    operatingCashflow: Optional[int]
    paymentsForOperatingActivities: Optional[int]
    proceedsFromOperatingActivities: Optional[int]
    changeInOperatingLiabilities: Optional[int]
    changeInOperatingAssets: Optional[int]
    depreciationDepletionAndAmortization: Optional[int]
    capitalExpenditures: Optional[int]
    changeInReceivables: Optional[int]
    changeInInventory: Optional[int]
    profitLoss: Optional[int]

    cashflowFromInvestment: Optional[int]
    cashflowFromFinancing: Optional[int]
    proceedsFromRepaymentsOfShortTermDebt: Optional[int]
    paymentsForRepurchaseOfCommonStock: Optional[int]
    paymentsForRepurchaseOfEquity: Optional[int]
    paymentsForRepurchaseOfPreferredStock: Optional[int]
    dividendPayout: Optional[int]
    dividendPayoutCommonStock: Optional[int]
    dividendPayoutPreferredStock: Optional[int]
    proceedsFromIssuanceOfCommonStock: Optional[int]
    proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet: Optional[int]
    proceedsFromIssuanceOfPreferredStock: Optional[int]
    proceedsFromRepurchaseOfEquity: Optional[int]
    proceedsFromSaleOfTreasuryStock: Optional[int]
    changeInCashAndCashEquivalents: Optional[int]
    changeInExchangeRate: Optional[int]

    netIncome: Optional[int]

# Output schema
class CashFlowStatementSchema(CashFlowStatementInput):
    id: UUID

    class Config:
        from_attributes = True
