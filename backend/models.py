from sqlalchemy import Column, Integer, String, DateTime
from .database import Base
from datetime import datetime

class Drug(Base):
    __tablename__ = "drugs"
    id = Column(Integer, primary_key=True, index=True)
    batch_id = Column(String, unique=True, index=True)
    dna_hash = Column(String, unique=True)
    manufacturer = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)