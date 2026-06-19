from fastapi import HTTPException
from app.models.event import Event
from app.repositories.event_repo import EventRepository


class EventService:

    @staticmethod
    def create(db, payload, current_user):
        event = Event(
            event_name=payload.event_name,
            description=payload.description,
            start_date=payload.start_date,
            end_date=payload.end_date,
            venue=payload.venue,
            capacity=payload.capacity,
            organizer_id=current_user.id,
            category_id=payload.category_id
        )
        return EventRepository.create(db, event)

    @staticmethod
    def get_all(db):
        return EventRepository.get_all(db)

    @staticmethod
    def get_by_id(db, event_id):
        event = EventRepository.get_by_id(db, event_id)
        if not event:
            raise HTTPException(status_code=404, detail="Event not found")
        return event

    @staticmethod
    def update(db, event_id, payload, current_user):
        event = EventRepository.get_by_id(db, event_id)
        if not event:
            raise HTTPException(status_code=404, detail="Event not found")
        if event.organizer_id != current_user.id and current_user.role.name != "Admin":
            raise HTTPException(status_code=403, detail="Permission denied")

        event.event_name = payload.event_name
        event.description = payload.description
        event.start_date = payload.start_date
        event.end_date = payload.end_date
        event.venue = payload.venue
        event.capacity = payload.capacity
        event.category_id = payload.category_id

        db.commit()
        db.refresh(event)
        return event

    @staticmethod
    def delete(db, event_id, current_user):
        event = EventRepository.get_by_id(db, event_id)
        if not event:
            raise HTTPException(status_code=404, detail="Event not found")
        if event.organizer_id != current_user.id and current_user.role.name != "Admin":
            raise HTTPException(status_code=403, detail="Permission denied")
        EventRepository.delete(db, event)
        return {"message": "Event deleted successfully"}

    @staticmethod
    def search(
        db,
        search=None,
        category_id=None,
        start_date=None,
        page=1,
        size=10,
        sort_by="start_date",
        order="asc"
    ):
        query = db.query(Event)

        if search:
            query = query.filter(Event.event_name.ilike(f"%{search}%"))
        if category_id:
            query = query.filter(Event.category_id == category_id)
        if start_date:
            query = query.filter(Event.start_date >= start_date)

        sort_col = getattr(Event, sort_by, Event.start_date)
        if order.lower() == "desc":
            query = query.order_by(sort_col.desc())
        else:
            query = query.order_by(sort_col.asc())

        offset = (page - 1) * size
        return query.offset(offset).limit(size).all()