# ==================== SCHEMAS ====================
# app/schemas/budget.py

from pydantic import BaseModel
from datetime import date

class BudgetBase(BaseModel):
    category: str
    amount: float
    date: date
    description: str | None = None
    vehicle_id: int

class BudgetCreate(BudgetBase):
    pass

class BudgetOut(BudgetBase):
    id: int

    class Config:
        orm_mode = True