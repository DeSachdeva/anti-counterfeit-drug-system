from pydantic import BaseModel
from datetime import date

class DrugCreate(BaseModel):
    name: str
    drug: str
    batch_id: str
    manufacturer: str
    mfg_date: date
    exp_date: date


class DrugOut(DrugCreate):
    id: int

    class Config:
        orm_mode = True

class DrugOutWithQR(DrugOut):
    qr_code_base64: str
