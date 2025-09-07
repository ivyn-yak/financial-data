from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import desc
from db import get_db
from models import EarningsCall, TranscriptSegment, Company
from schemas.earnings_transcript import EarningsCallSchema, TranscriptSegmentSchema
from typing import List
from uuid import UUID

router = APIRouter(prefix="/earnings")

@router.get("/", response_model=List[EarningsCallSchema])
def get_all_earnings_calls(db: Session = Depends(get_db)):
    return db.query(EarningsCall).all()

@router.get("/{symbol}", response_model=List[EarningsCallSchema])
def get_earnings_calls_by_ticker(symbol: str, db: Session = Depends(get_db)):
    earnings_calls_list = (
        db.query(EarningsCall)
        .join(Company)
        .filter(Company.Symbol == symbol)
        .all()
    )
    return earnings_calls_list

@router.get("/transcript/{earnings_call_id}", response_model=List[TranscriptSegmentSchema])
def get_earnings_calls_by_ticker(earnings_call_id: UUID, db: Session = Depends(get_db)):
    earnings_calls_list = (
        db.query(TranscriptSegment)
        .filter(TranscriptSegment.earnings_call_id == earnings_call_id)
        .all()
    )
    return earnings_calls_list


