# ==================== CRUD ====================
# app/crud/maintenance.py

from sqlalchemy.orm import Session
from ..models.maintenance import Maintenance
from ..schemas.maintenance import MaintenanceCreate

def create_maintenance(db: Session, data: MaintenanceCreate):
    record = Maintenance(**data.dict())
    db.add(record)
    db.commit()
    db.refresh(record)
    return record

def get_maintenances(db: Session):
    return db.query(Maintenance).all()

def get_maintenance(db: Session, maintenance_id: int):
    return db.query(Maintenance).filter(Maintenance.id == maintenance_id).first()

def delete_maintenance(db: Session, maintenance_id: int):
    record = db.query(Maintenance).filter(Maintenance.id == maintenance_id).first()
    if record:
        db.delete(record)
        db.commit()
    return record
