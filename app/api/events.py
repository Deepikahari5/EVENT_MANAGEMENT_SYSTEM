from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Optional
from datetime import datetime

from app.database.database import get_db
from app.schemas.event import EventCreate, EventUpdate
from app.services.event_service import EventService
from app.core.permissions import admin_or_organizer
from app.core.dependencies import get_current_user

router = APIRouter(
    prefix="/events",
    tags=["Events"]
)


@router.post("/")
def create_event(
    payload: EventCreate,
    db: Session = Depends(get_db),
    current_user=Depends(admin_or_organizer)
):
    return EventService.create(db, payload, current_user)


@router.get("/search")
def search_events(
    search: Optional[str] = None,
    category_id: Optional[int] = None,
    start_date: Optional[datetime] = None,
    page: int = 1,
    size: int = 10,
    sort_by: str = "start_date",
    order: str = "asc",
    db: Session = Depends(get_db)
):
    return EventService.search(db, search, category_id, start_date, page, size, sort_by, order)


@router.get("/")
def get_events(db: Session = Depends(get_db)):
    return EventService.get_all(db)


@router.get("/{event_id}")
def get_event(event_id: int, db: Session = Depends(get_db)):
    return EventService.get_by_id(db, event_id)


@router.put("/{event_id}")
def update_event(
    event_id: int,
    payload: EventUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(admin_or_organizer)
):
    return EventService.update(db, event_id, payload, current_user)


@router.delete("/{event_id}")
def delete_event(
    event_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(admin_or_organizer)
):
    return EventService.delete(db, event_id, current_user)