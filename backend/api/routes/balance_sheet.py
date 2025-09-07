from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import desc

from db import get_db
from models import BalanceSheet, Company
from schemas import BalanceSheetSchema
from schemas.enums import Period

router = APIRouter(prefix="/balance_sheet")

@router.get("/", response_model=List[BalanceSheetSchema])
def get_all_balance_sheets(db: Session = Depends(get_db)):
    return db.query(BalanceSheet).all()

@router.get("/{symbol}", response_model=List[BalanceSheetSchema])
def get_balance_sheet(
    symbol: str,
    period: Period,
    k: Optional[int] = Query(5, gt=0),
    db: Session = Depends(get_db),
):
    balance_sheet_list = (
        db.query(BalanceSheet)
        .join(Company)
        .filter(Company.Symbol == symbol, BalanceSheet.period == period)
        .order_by(desc(BalanceSheet.fiscalDateEnding))
        .limit(k)
        .all()
    )

    if not balance_sheet_list:
        raise HTTPException(status_code=404, detail=f"No {period} balance sheet found for {symbol}")

    return balance_sheet_list
