# ==================== SCHEMAS ====================
# app/schemas/fuel_log.py

from pydantic import BaseModel
from datetime import date

class FuelLogBase(BaseModel):
    vehicle_id: int
    date: date
    fuel_type: str
    volume: float
    cost: float

class FuelLogCreate(FuelLogBase):
    pass

class FuelLogOut(FuelLogBase):
    id: int

    class Config:
        orm_mode = True

