from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.services.registration_service import RegistrationService
from app.core.permissions import participant_only
from app.core.dependencies import get_current_user

router = APIRouter(
    prefix="/registrations",
    tags=["Registrations"]
)


@router.post("/register/{event_id}")
def register_event(
    event_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(participant_only)
):
    return RegistrationService.register(db, event_id, current_user)


@router.get("/my")
def my_registrations(
    db: Session = Depends(get_db),
    current_user=Depends(participant_only)
):
    return RegistrationService.my_registrations(db, current_user)


@router.delete("/{registration_id}")
def cancel_registration(
    registration_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(participant_only)
):
    return RegistrationService.cancel(db, registration_id, current_user)