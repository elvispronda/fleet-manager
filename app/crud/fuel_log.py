# ==================== CRUD ====================
# app/crud/fuel_log.py

from sqlalchemy.orm import Session
from ..models.fuel_log import FuelLog
from ..schemas.fuel_log import FuelLogCreate

def create_fuel_log(db: Session, log: FuelLogCreate):
    db_log = FuelLog(**log.dict())
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log

def get_fuel_logs(db: Session):
    return db.query(FuelLog).all()

def get_fuel_log(db: Session, log_id: int):
    return db.query(FuelLog).filter(FuelLog.id == log_id).first()

def delete_fuel_log(db: Session, log_id: int):
    log = db.query(FuelLog).filter(FuelLog.id == log_id).first()
    if log:
        db.delete(log)
        db.commit()
    return log

