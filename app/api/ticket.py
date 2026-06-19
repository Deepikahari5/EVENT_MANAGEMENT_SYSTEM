from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.services.ticket_service import TicketService
from app.core.permissions import admin_or_organizer
from app.core.dependencies import get_current_user

router = APIRouter(
    prefix="/tickets",
    tags=["Tickets"]
)


@router.post("/generate/{registration_id}")
def generate_ticket(
    registration_id: int,
    db: Session = Depends(get_db),
    user=Depends(admin_or_organizer)
):
    return TicketService.generate(db, registration_id)


@router.get("/{ticket_id}")
def get_ticket(
    ticket_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return TicketService.get_ticket(db, ticket_id)


@router.get("/validate/{ticket_id}")
def validate_ticket(
    ticket_id: int,
    db: Session = Depends(get_db),
    user=Depends(admin_or_organizer)
):
    return TicketService.validate_ticket(db, ticket_id)


@router.delete("/cancel/{ticket_id}")
def cancel_ticket(
    ticket_id: int,
    db: Session = Depends(get_db),
    user=Depends(admin_or_organizer)
):
    return TicketService.cancel_ticket(db, ticket_id)