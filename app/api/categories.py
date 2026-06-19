from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.category import CategoryCreate
from app.services.category_service import CategoryService

router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)


@router.post("/")
def create_category(
    payload: CategoryCreate,
    db: Session = Depends(get_db)
):
    return CategoryService.create(
        db,
        payload
    )