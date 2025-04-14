# ==================== CRUD ====================
# app/crud/budget.py

from sqlalchemy.orm import Session
from ..models.budget import BudgetEntry
from ..schemas.budget import BudgetCreate

def create_budget_entry(db: Session, entry: BudgetCreate):
    db_entry = BudgetEntry(**entry.dict())
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry

def get_budget_entries(db: Session):
    return db.query(BudgetEntry).all()

def get_budget_entry(db: Session, entry_id: int):
    return db.query(BudgetEntry).filter(BudgetEntry.id == entry_id).first()

def delete_budget_entry(db: Session, entry_id: int):
    entry = db.query(BudgetEntry).filter(BudgetEntry.id == entry_id).first()
    if entry:
        db.delete(entry)
        db.commit()
    return entry