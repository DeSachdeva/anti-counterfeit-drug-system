from pydantic import BaseModel
from datetime import date

class DrugCreate(BaseModel):
    name: str
    drug: str
    batch_id: str
    manufacturer: str
    mfg_date: date
    exp_date: date
    hash: str

class DrugOut(DrugCreate):
    id: int

    class Config:
        orm_mode = True
