from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.category import CategoryCreate
from app.services.category_service import CategoryService
from app.core.permissions import admin_or_organizer
from app.core.dependencies import get_current_user

router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)


@router.post("/")
def create_category(
    payload: CategoryCreate,
    db: Session = Depends(get_db),
    user=Depends(admin_or_organizer)
):
    return CategoryService.create(db, payload)


@router.get("/")
def list_categories(
    db: Session = Depends(get_db)
):
    return CategoryService.get_all(db)


@router.get("/{category_id}")
def get_category(
    category_id: int,
    db: Session = Depends(get_db)
):
    return CategoryService.get_by_id(db, category_id)


@router.delete("/{category_id}")
def delete_category(
    category_id: int,
    db: Session = Depends(get_db),
    user=Depends(admin_or_organizer)
):
    return CategoryService.delete(db, category_id)
