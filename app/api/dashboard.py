from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.services.dashboard_service import (
    DashboardService
)

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/summary")
def dashboard_summary(
    db: Session = Depends(get_db)
):
    return DashboardService.summary(
        db
    )