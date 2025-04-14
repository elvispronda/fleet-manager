
# ==================== SCHEMAS ====================
# app/schemas/user.py

from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    full_name: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    role: str

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    username: str
    password: str