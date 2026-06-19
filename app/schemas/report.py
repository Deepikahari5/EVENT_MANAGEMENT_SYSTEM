from pydantic import BaseModel


class EventReport(BaseModel):
    event_id: int
    event_name: str
    registrations: int


class AttendanceReport(BaseModel):
    event_id: int
    event_name: str
    attendance_count: int