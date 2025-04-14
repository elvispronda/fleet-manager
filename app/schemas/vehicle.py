
# ==================== SCHEMAS ====================
# app/schemas/vehicle.py

from pydantic import BaseModel

class VehicleBase(BaseModel):
    make: str
    model: str
    year: int
    plate_number: str
    mileage: float = 0.0
    status: str = "available"

class VehicleCreate(VehicleBase):
    pass

class VehicleOut(VehicleBase):
    id: int

    class Config:
        orm_mode = True
