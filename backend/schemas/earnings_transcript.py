from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID

class TranscriptSegmentBase(BaseModel):
    speaker: Optional[str] = None
    title: Optional[str] = None
    content: str
    sentiment: Optional[float] = None

class TranscriptSegmentInput(TranscriptSegmentBase):
    pass

class TranscriptSegmentSchema(TranscriptSegmentBase):
    id: UUID
    class Config:
        from_attributes = True


class EarningsCallBase(BaseModel):
    company_id: UUID
    quarter: str

class EarningsCallInput(EarningsCallBase):
    transcript_segment: List[TranscriptSegmentInput]

class EarningsCallSchema(EarningsCallBase):
    id: UUID
    transcript_segment: List[TranscriptSegmentSchema]
    class Config:
        from_attributes = True
