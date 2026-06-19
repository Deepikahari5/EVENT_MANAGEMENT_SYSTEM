from pydantic import BaseModel
from datetime import datetime


class RegistrationResponse(BaseModel):
    id: int
    user_id: int
    event_id: int
    status: str
    registered_at: datetime

    class Config:
        from_attributes = True