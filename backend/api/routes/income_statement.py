from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import desc

from db import get_db
from models import IncomeStatement, Company
from schemas import IncomeStatementSchema
from schemas.enums import Period

router = APIRouter(prefix="/income_statement")

@router.get("/", response_model=List[IncomeStatementSchema])
def get_all_income_statements(db: Session = Depends(get_db)):
    return db.query(IncomeStatement).all()

@router.get("/{symbol}", response_model=List[IncomeStatementSchema])
def get_income_statement(
    symbol: str,
    period: Period,
    k: Optional[int] = Query(5, gt=0),
    db: Session = Depends(get_db),
):
    income_statement_list = (
        db.query(IncomeStatement)
        .join(Company)
        .filter(Company.Symbol == symbol, IncomeStatement.period == period)
        .order_by(desc(IncomeStatement.fiscalDateEnding))
        .limit(k)
        .all()
    )

    if not income_statement_list:
        raise HTTPException(status_code=404, detail=f"No {period} income statement found for {symbol}")

    return income_statement_list
