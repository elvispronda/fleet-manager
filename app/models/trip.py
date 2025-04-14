# ==================== TRIP MODULE ====================

# app/models/trip.py
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from ..database import Base

class Trip(Base):
    __tablename__ = "trips"
    id = Column(Integer, primary_key=True, index=True)
    origin = Column(String, nullable=False)
    destination = Column(String, nullable=False)
    departure_date = Column(Date, nullable=False)
    return_date = Column(Date)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))
    driver_id = Column(Integer, ForeignKey("users.id"))

# app/schemas/trip.py
from pydantic import BaseModel
from datetime import date

class TripBase(BaseModel):
    origin: str
    destination: str
    departure_date: date
    return_date: date | None = None
    vehicle_id: int
    driver_id: int

class TripCreate(TripBase):
    pass

class TripOut(TripBase):
    id: int

    class Config:
        orm_mode = True

# app/crud/trip.py
from sqlalchemy.orm import Session
from ..models.trip import Trip
from ..schemas.trip import TripCreate

def create_trip(db: Session, trip: TripCreate):
    db_trip = Trip(**trip.dict())
    db.add(db_trip)
    db.commit()
    db.refresh(db_trip)
    return db_trip

def get_trips(db: Session):
    return db.query(Trip).all()

def get_trip(db: Session, trip_id: int):
    return db.query(Trip).filter(Trip.id == trip_id).first()

def delete_trip(db: Session, trip_id: int):
    trip = db.query(Trip).filter(Trip.id == trip_id).first()
    if trip:
        db.delete(trip)
        db.commit()
    return trip

# app/api/trip.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas import trip as schema
from ..crud import trip as crud
from ..auth.dependencies import get_current_user
from ..database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schema.TripOut)
def create_trip(trip: schema.TripCreate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    return crud.create_trip(db, trip)

@router.get("/", response_model=list[schema.TripOut])
def read_trips(db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    return crud.get_trips(db)

@router.get("/{trip_id}", response_model=schema.TripOut)
def read_trip(trip_id: int, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    db_trip = crud.get_trip(db, trip_id)
    if db_trip is None:
        raise HTTPException(status_code=404, detail="Trip not found")
    return db_trip

@router.delete("/{trip_id}", response_model=schema.TripOut)
def delete_trip(trip_id: int, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    deleted_trip = crud.delete_trip(db, trip_id)
    if deleted_trip is None:
        raise HTTPException(status_code=404, detail="Trip not found")
    return deleted_trip
