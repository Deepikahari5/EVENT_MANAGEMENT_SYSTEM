from pydantic import BaseModel
from datetime import datetime


class TicketResponse(BaseModel):
    id: int
    ticket_number: str
    registration_id: int
    status: str
    issued_at: datetime

    class Config:
        from_attributes = True