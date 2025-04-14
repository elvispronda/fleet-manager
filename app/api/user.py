
# ==================== API ROUTES ====================
# app/api/user.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..schemas import user as schema
from ..crud import user as crud
from ..auth.dependencies import get_current_user
from ..database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schema.UserOut)
def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db, user)

@router.get("/", response_model=list[schema.UserOut])
def read_users(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return crud.get_users(db)

@router.get("/me", response_model=schema.UserOut)
def read_current_user(current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    return crud.get_user_by_username(db, current_user["sub"])
