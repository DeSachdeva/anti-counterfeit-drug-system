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

from schemas import DrugOutWithQR

@router.delete("/admin/delete_all_drugs")
def delete_all_drugs(db: Session = Depends(get_db)):
    db.query(Drug).delete()
    db.commit()
    return {"message": "All drugs deleted."}
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

from schemas import DrugOutWithQR

@router.post("/register", response_model=DrugOutWithQR)
def register_drug(drug: DrugCreate, db: Session = Depends(get_db)):

    if db.query(Drug).filter(Drug.batch_id == drug.batch_id).first():
        raise HTTPException(status_code=400, detail="Batch ID already registered")

    new_drug = Drug(
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
        "mfg_date": new_drug.mfg_date.strftime("%d-%m-%Y") if hasattr(new_drug.mfg_date, 'strftime') else str(new_drug.mfg_date),
        "exp_date": new_drug.exp_date.strftime("%d-%m-%Y") if hasattr(new_drug.exp_date, 'strftime') else str(new_drug.exp_date),
        "hash": new_drug.hash
    }

    qr_b64 = generate_qr(qr_data, new_drug.id)


    result = new_drug.__dict__.copy()
    result['qr_code_base64'] = qr_b64
    return result

@router.get("/verify/{dna_hash}", response_model=DrugOut)
def verify_dna(dna_hash: str, db: Session = Depends(get_db)):
    drug = db.query(Drug).filter(Drug.hash == dna_hash).first()
    if not drug:
        raise HTTPException(status_code=404, detail="Drug not found")
    return drug
