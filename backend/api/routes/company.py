from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from models import Company
from schemas.company import CompanySchema
from typing import List
from uuid import UUID 

router = APIRouter(prefix="/company")

@router.get("/", response_model=List[CompanySchema])
def get_all_companies(db: Session = Depends(get_db)):
    return db.query(Company).all()

@router.get("/{symbol}", response_model=CompanySchema)
def get_company(symbol: str, db: Session = Depends(get_db)):
    return db.query(Company).filter(Company.Symbol == symbol).first()
