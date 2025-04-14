# ==================== API ROUTES ====================
# app/api/budget.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas import budget as schema
from ..crud import budget as crud
from ..auth.dependencies import get_current_user
from ..database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schema.BudgetOut)
def create_budget_entry(entry: schema.BudgetCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return crud.create_budget_entry(db, entry)

@router.get("/", response_model=list[schema.BudgetOut])
def read_budget_entries(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return crud.get_budget_entries(db)

@router.get("/{entry_id}", response_model=schema.BudgetOut)
def read_budget_entry(entry_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    db_entry = crud.get_budget_entry(db, entry_id)
    if db_entry is None:
        raise HTTPException(status_code=404, detail="Budget entry not found")
    return db_entry

@router.delete("/{entry_id}", response_model=schema.BudgetOut)
def delete_budget_entry(entry_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    deleted_entry = crud.delete_budget_entry(db, entry_id)
    if deleted_entry is None:
        raise HTTPException(status_code=404, detail="Budget entry not found")
    return deleted_entry
