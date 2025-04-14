# ==================== MODELS ====================
# app/models/budget.py

from sqlalchemy import Column, Integer, Float, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class BudgetEntry(Base):
    __tablename__ = "budget_entries"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, nullable=False)  # e.g., fuel, maintenance, insurance
    amount = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    description = Column(String)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"), nullable=False)

