from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Drug
from schemas import DrugCreate, DrugOut

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=DrugOut)
def register_drug(drug: DrugCreate, db: Session = Depends(get_db)):
    db_drug = db.query(Drug).filter(Drug.batch_id == drug.batch_id).first()
    if db_drug:
        raise HTTPException(status_code=400, detail="Batch already registered")

    new_drug = Drug(
        name=drug.name,
        drug=drug.drug,
        batch_id=drug.batch_id,
        manufacturer=drug.manufacturer,
        mfg_date=drug.mfg_date,
        exp_date=drug.exp_date,
        hash="temp_hash"  # placeholder until QR/hash logic is connected
    )

    db.add(new_drug)
    db.commit()
    db.refresh(new_drug)
    return new_drug

@router.get("/verify/{dna_hash}", response_model=DrugOut)
def verify_dna(dna_hash: str, db: Session = Depends(get_db)):
    drug = db.query(Drug).filter(Drug.hash == dna_hash).first()
    if not drug:
        raise HTTPException(status_code=404, detail="Drug not found")
    return drug
