
# ==================== API ROUTES ====================
# app/api/vehicle.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas import vehicle as schema
from ..crud import vehicle as crud
from ..auth.dependencies import get_current_user
from ..database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schema.VehicleOut)
def create_vehicle(vehicle: schema.VehicleCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return crud.create_vehicle(db, vehicle)

@router.get("/", response_model=list[schema.VehicleOut])
def read_vehicles(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return crud.get_vehicles(db)

@router.get("/{vehicle_id}", response_model=schema.VehicleOut)
def read_vehicle(vehicle_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    db_vehicle = crud.get_vehicle(db, vehicle_id)
    if db_vehicle is None:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return db_vehicle

@router.delete("/{vehicle_id}", response_model=schema.VehicleOut)
def delete_vehicle(vehicle_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    deleted_vehicle = crud.delete_vehicle(db, vehicle_id)
    if deleted_vehicle is None:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return deleted_vehicle
