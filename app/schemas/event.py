from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class EventCreate(BaseModel):
    event_name: str
    description: str
    start_date: datetime
    end_date: datetime
    venue: str
    capacity: int
    category_id: int


class EventUpdate(BaseModel):
    event_name: str
    description: str
    start_date: datetime
    end_date: datetime
    venue: str
    capacity: int
    category_id: int


class EventResponse(BaseModel):
    id: int
    event_name: str
    description: str
    venue: str
    capacity: int
    start_date: datetime
    end_date: datetime
    status: str
    organizer_id: int
    category_id: int

    class Config:
        from_attributes = True