from sqlalchemy import Column, Integer, String, Date
from database import Base

class Drug(Base):
    __tablename__ = "drugs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    drug = Column(String)
    batch_id = Column(String, unique=True, index=True)
    manufacturer = Column(String)
    mfg_date = Column(Date)
    exp_date = Column(Date)
    hash = Column(String, unique=True, index=True)
