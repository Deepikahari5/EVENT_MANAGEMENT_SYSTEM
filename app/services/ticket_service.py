from fastapi import HTTPException
from app.models.ticket import Ticket
from app.repositories.ticket_repo import TicketRepository
from app.repositories.registration_repo import RegistrationRepository
import uuid


class TicketService:

    @staticmethod
    def generate(db, registration_id):

        registration = RegistrationRepository.get_by_id(db, registration_id)

        if not registration:
            raise HTTPException(status_code=404, detail="Registration not found")

        if registration.status == "Cancelled":
            raise HTTPException(status_code=400, detail="Registration is cancelled")

        existing_ticket = TicketRepository.get_by_registration(db, registration_id)
        if existing_ticket:
            raise HTTPException(status_code=400, detail="Ticket already exists for this registration")

        ticket_number = f"TKT-{str(uuid.uuid4()).upper()[:8]}"

        ticket = Ticket(
            ticket_number=ticket_number,
            registration_id=registration_id,
            status="Active"
        )

        return TicketRepository.create(db, ticket)

    @staticmethod
    def get_ticket(db, ticket_id):
        ticket = TicketRepository.get_by_id(db, ticket_id)
        if not ticket:
            raise HTTPException(status_code=404, detail="Ticket not found")
        return ticket

    @staticmethod
    def validate_ticket(db, ticket_id):
        ticket = TicketRepository.get_by_id(db, ticket_id)
        if not ticket:
            raise HTTPException(status_code=404, detail="Ticket not found")
        return {"valid": ticket.status == "Active", "ticket": ticket}

    @staticmethod
    def cancel_ticket(db, ticket_id):
        ticket = TicketRepository.get_by_id(db, ticket_id)
        if not ticket:
            raise HTTPException(status_code=404, detail="Ticket not found")
        if ticket.status == "Cancelled":
            raise HTTPException(status_code=400, detail="Ticket already cancelled")
        ticket.status = "Cancelled"
        db.commit()
        db.refresh(ticket)
        return ticket