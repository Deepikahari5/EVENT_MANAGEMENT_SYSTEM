from pydantic import BaseModel


class DashboardResponse(BaseModel):

    total_events: int

    total_participants: int

    upcoming_events: int

    completed_events: int