from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.services.report_service import (
    ReportService
)

from app.core.permissions import (
    admin_or_organizer
)

router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)


@router.get("/events")
def event_report(
    db: Session = Depends(get_db),
    user=Depends(admin_or_organizer)
):
    return ReportService.event_report(
        db
    )


@router.get("/attendance")
def attendance_report(
    db: Session = Depends(get_db),
    user=Depends(admin_or_organizer)
):
    return ReportService.attendance_report(
        db
    )


@router.get("/registrations")
def registration_report(
    db: Session = Depends(get_db),
    user=Depends(admin_or_organizer)
):
    return ReportService.registration_report(
        db
    )