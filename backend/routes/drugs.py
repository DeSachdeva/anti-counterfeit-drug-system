from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=schemas.DrugOut)
def register_drug(drug: schemas.DrugCreate, db: Session = Depends(get_db)):
    db_drug = db.query(models.Drug).filter(models.Drug.batch_id == drug.batch_id).first()
    if db_drug:
        raise HTTPException(status_code=400, detail="Batch already registered")

    new_drug = models.Drug(**drug.model_dump())
    db.add(new_drug)
    db.commit()
    db.refresh(new_drug)
    return new_drug

@router.get("/verify/{dna_hash}", response_model=schemas.DrugOut)
def verify_dna(dna_hash: str, db: Session = Depends(get_db)):
    drug = db.quer(models.Drug).filter(models.Drug.dna_hash == dna_hash).first()
    if not drug:
        raise HTTPException(status_code=404, detail="Drug not found")

    return drug