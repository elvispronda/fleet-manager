# ==================== API ROUTES ====================
# app/api/fuel_log.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas import fuel_log as schema
from ..crud import fuel_log as crud
from ..auth.dependencies import get_current_user
from ..database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schema.FuelLogOut)
def create_fuel_log(log: schema.FuelLogCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return crud.create_fuel_log(db, log)

@router.get("/", response_model=list[schema.FuelLogOut])
def read_fuel_logs(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return crud.get_fuel_logs(db)

@router.get("/{log_id}", response_model=schema.FuelLogOut)
def read_fuel_log(log_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    db_log = crud.get_fuel_log(db, log_id)
    if db_log is None:
        raise HTTPException(status_code=404, detail="Fuel log not found")
    return db_log

@router.delete("/{log_id}", response_model=schema.FuelLogOut)
def delete_fuel_log(log_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    deleted_log = crud.delete_fuel_log(db, log_id)
    if deleted_log is None:
        raise HTTPException(status_code=404, detail="Fuel log not found")
    return deleted_log
