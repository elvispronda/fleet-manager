# ==================== MODELS ====================
# app/models/fuel_log.py

from sqlalchemy import Column, Integer, Float, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class FuelLog(Base):
    __tablename__ = "fuel_logs"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"), nullable=False)
    date = Column(Date, nullable=False)
    fuel_type = Column(String, nullable=False)
    volume = Column(Float, nullable=False)  # in liters
    cost = Column(Float, nullable=False)


