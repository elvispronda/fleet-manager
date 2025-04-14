# ==================== FUEL MODULE ====================

# app/models/fuel.py
from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base
from datetime import datetime

class FuelLog(Base):
    __tablename__ = "fuel_logs"
    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))
    quantity = Column(Float, nullable=False)
    cost = Column(Float, nullable=False)
    date = Column(DateTime, default=datetime.utcnow)

# app/schemas/fuel.py
from pydantic import BaseModel
from datetime import datetime

class FuelLogBase(BaseModel):
    vehicle_id: int
    quantity: float
    cost: float

class FuelLogCreate(FuelLogBase):
    pass

class FuelLogOut(FuelLogBase):
    id: int
    date: datetime

    class Config:
        orm_mode = True

# app/crud/fuel.py
from sqlalchemy.orm import Session
from ..models.fuel import FuelLog
from ..schemas.fuel import FuelLogCreate

def create_fuel_log(db: Session, log: FuelLogCreate):
    db_log = FuelLog(**log.dict())
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log

def get_fuel_logs(db: Session):
    return db.query(FuelLog).all()

# app/api/fuel.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas import fuel as schema
from ..crud import fuel as crud
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
def create_log(log: schema.FuelLogCreate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    return crud.create_fuel_log(db, log)

@router.get("/", response_model=list[schema.FuelLogOut])
def read_logs(db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    return crud.get_fuel_logs(db)
