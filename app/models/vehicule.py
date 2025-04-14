# ==================== MODELS ====================
# app/models/vehicle.py

from sqlalchemy import Column, Integer, String, Float
from ..database import Base

class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    make = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer)
    plate_number = Column(String, unique=True, nullable=False)
    mileage = Column(Float, default=0.0)
    status = Column(String, default="available")  # available, in_use, maintenance
