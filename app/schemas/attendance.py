from pydantic import BaseModel
from datetime import datetime


class AttendanceCreate(BaseModel):
    ticket_id: int


class AttendanceResponse(BaseModel):
    id: int
    event_id: int
    user_id: int
    status: str
    attendance_time: datetime

    class Config:
        from_attributes = True