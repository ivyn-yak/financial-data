from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import desc

from db import get_db
from models import CashFlowStatement, Company
from schemas import CashFlowStatementSchema
from schemas.enums import Period

router = APIRouter(prefix="/cash_flow")

@router.get("/", response_model=List[CashFlowStatementSchema])
def get_all_cash_flows(db: Session = Depends(get_db)):
    return db.query(CashFlowStatement).all()

@router.get("/{symbol}", response_model=List[CashFlowStatementSchema])
def get_cash_flow(
    symbol: str,
    period: Period,
    k: Optional[int] = Query(5, gt=0),
    db: Session = Depends(get_db),
):
    cash_flow_list = (
        db.query(CashFlowStatement)
        .join(Company)
        .filter(Company.Symbol == symbol, CashFlowStatement.period == period)
        .order_by(desc(CashFlowStatement.fiscalDateEnding))
        .limit(k)
        .all()
    )

    if not cash_flow_list:
        raise HTTPException(status_code=404, detail=f"No {period} cash flow found for {symbol}")

    return cash_flow_list
