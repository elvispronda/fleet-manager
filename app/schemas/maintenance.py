# ==================== SCHEMAS ====================
# app/schemas/maintenance.py

from pydantic import BaseModel
from datetime import date

class MaintenanceBase(BaseModel):
    vehicle_id: int
    description: str
    cost: float
    maintenance_date: date

class MaintenanceCreate(MaintenanceBase):
    pass

class MaintenanceOut(MaintenanceBase):
    id: int

    class Config:
        orm_mode = True
