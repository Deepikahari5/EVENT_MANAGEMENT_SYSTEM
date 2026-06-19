from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.attendance import AttendanceCreate
from app.services.attendance_service import AttendanceService
from app.core.permissions import admin_or_organizer
from app.core.dependencies import get_current_user

router = APIRouter(
    prefix="/attendance",
    tags=["Attendance"]
)


@router.post("/mark")
def mark_attendance(
    payload: AttendanceCreate,
    db: Session = Depends(get_db),
    user=Depends(admin_or_organizer)
):
    return AttendanceService.mark_attendance(db, payload.ticket_id)


@router.get("/event/{event_id}")
def get_event_attendance(
    event_id: int,
    db: Session = Depends(get_db),
    user=Depends(admin_or_organizer)
):
    return AttendanceService.get_event_attendance(db, event_id)


@router.get("/summary/{event_id}")
def attendance_summary(
    event_id: int,
    db: Session = Depends(get_db)
):
    return AttendanceService.summary(db, event_id)