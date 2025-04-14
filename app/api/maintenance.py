# ==================== API ROUTES ====================
# app/api/maintenance.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas import maintenance as schema
from ..crud import maintenance as crud
from ..auth.dependencies import get_current_user
from ..database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schema.MaintenanceOut)
def create_maintenance(data: schema.MaintenanceCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return crud.create_maintenance(db, data)

@router.get("/", response_model=list[schema.MaintenanceOut])
def read_maintenances(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return crud.get_maintenances(db)

@router.get("/{maintenance_id}", response_model=schema.MaintenanceOut)
def read_maintenance(maintenance_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    record = crud.get_maintenance(db, maintenance_id)
    if not record:
        raise HTTPException(status_code=404, detail="Maintenance record not found")
    return record

@router.delete("/{maintenance_id}", response_model=schema.MaintenanceOut)
def delete_maintenance(maintenance_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    deleted = crud.delete_maintenance(db, maintenance_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Maintenance record not found")
    return deleted
