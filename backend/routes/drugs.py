from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Drug
from schemas import DrugCreate, DrugOut
from qr_generator import generate_qr
from hash_dna import hashed_dna

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=DrugOut)
def register_drug(drug: DrugCreate, db: Session = Depends(get_db)):
    db_drug = db.query(drug).filter(drug.id == drug.id).first()
    if db_drug:
        raise HTTPException(status_code=400, detail="ID already registered")

    new_drug = drug(
        id=drug.id,
        name=drug.name,
        drug=drug.drug,
        batch_id=drug.batch_id,
        manufacturer=drug.manufacturer,
        mfg_date=drug.mfg_date,
        exp_date=drug.exp_date,
        hash=hashed_dna()
    )

    db.add(new_drug)
    db.commit()
    db.refresh(new_drug)

    qr_data = {
        "id": new_drug.id,
        "name": new_drug.name,
        "drug": new_drug.drug,
        "batch_id": new_drug.batch_id,
        "manufacturer": new_drug.manufacturer,
        "mfg_date": str(new_drug.mfg_date),
        "exp_date": str(new_drug.exp_date),
        "hash": new_drug.hash
    }

    generate_qr(qr_data, new_drug.id)

    return new_drug

@router.get("/verify/{dna_hash}", response_model=DrugOut)
def verify_dna(dna_hash: str, db: Session = Depends(get_db)):
    drug = db.query(drug).filter(drug.hash == dna_hash).first()
    if not drug:
        raise HTTPException(status_code=404, detail="Drug not found")
    return drug
