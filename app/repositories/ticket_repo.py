from sqlalchemy.orm import Session
from app.models.ticket import Ticket


class TicketRepository:

    @staticmethod
    def create(db: Session, ticket):
        db.add(ticket)
        db.commit()
        db.refresh(ticket)
        return ticket

    @staticmethod
    def get_by_id(db: Session, ticket_id: int):
        return (
            db.query(Ticket)
            .filter(Ticket.id == ticket_id)
            .first()
        )

    @staticmethod
    def get_by_registration(db: Session, registration_id: int):
        return (
            db.query(Ticket)
            .filter(Ticket.registration_id == registration_id)
            .first()
        )

    @staticmethod
    def count(db: Session):
        return db.query(Ticket).count()