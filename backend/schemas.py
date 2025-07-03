from pydantic import BaseModel

class DrugBase(BaseModel):
    batch_id: str
    dna_hash: str
    manufacturer: str

class DrugCreate(DrugBase):
    pass

class DrugOut(DrugBase):
    id: int

    class Config:
        orm_mode = True