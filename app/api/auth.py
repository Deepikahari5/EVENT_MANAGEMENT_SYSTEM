from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.auth import RegisterSchema, LoginSchema
from app.services.auth_service import AuthService
from app.core.dependencies import get_current_user
from app.core.permissions import admin_only
from app.models.user import User

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(
    payload: RegisterSchema,
    db: Session = Depends(get_db)
):
    return AuthService.register(db, payload)


@router.post("/login")
def login(
    payload: LoginSchema,
    db: Session = Depends(get_db)
):
    return AuthService.login(db, payload)


@router.get("/me")
def get_me(current_user=Depends(get_current_user)):
    return {
        "id": current_user.id,
        "full_name": current_user.full_name,
        "email": current_user.email,
        "role": current_user.role.name,
        "is_active": current_user.is_active,
        "created_at": str(current_user.created_at)
    }


@router.get("/make-admin/{user_id}")
def make_admin(
    user_id: int,
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.role_id = 1
    db.commit()
    db.refresh(user)
    return {"message": f"{user.email} is now Admin", "role_id": user.role_id}


@router.get("/admin-test")
def admin_test(current_user=Depends(admin_only)):
    return {"message": f"Welcome Admin {current_user.full_name}"}