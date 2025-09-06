import uuid
from sqlalchemy import Column, String, Text, Float, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from db import Base

class EarningsCall(Base):
    __tablename__ = "earnings_call"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    company_id = Column(UUID(as_uuid=True), ForeignKey("company.id"), nullable=False)
    quarter = Column(String(10), nullable=False)

    transcript_segment = relationship("TranscriptSegment", back_populates="earnings_call")


class TranscriptSegment(Base):
    __tablename__ = "transcript_segment"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    earnings_call_id = Column(UUID(as_uuid=True), ForeignKey("earnings_call.id"), nullable=False)

    speaker = Column(String(255))
    title = Column(String(255))
    content = Column(Text, nullable=False)
    sentiment = Column(Float)

    earnings_call = relationship("EarningsCall", back_populates="transcript_segment")
