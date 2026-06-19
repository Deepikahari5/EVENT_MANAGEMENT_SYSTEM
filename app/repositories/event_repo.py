from sqlalchemy.orm import Session
from app.models.event import Event


class EventRepository:

    @staticmethod
    def create(db: Session, event):
        db.add(event)
        db.commit()
        db.refresh(event)
        return event

    @staticmethod
    def get_all(db: Session):
        return db.query(Event).all()

    @staticmethod
    def get_by_id(
        db: Session,
        event_id: int
    ):
        return db.query(Event).filter(
            Event.id == event_id
        ).first()

    @staticmethod
    def delete(
        db: Session,
        event
    ):
        db.delete(event)
        db.commit()