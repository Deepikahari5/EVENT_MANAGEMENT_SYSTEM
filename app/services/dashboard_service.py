from datetime import datetime
from sqlalchemy import func
from app.models.event import Event
from app.models.registration import Registration
from app.models.user import User


class DashboardService:

    @staticmethod
    def summary(db):

        total_events = db.query(Event).count()

        total_participants = (
            db.query(Registration.user_id)
            .distinct()
            .count()
        )

        upcoming_events = (
            db.query(Event)
            .filter(Event.start_date > datetime.utcnow())
            .count()
        )

        completed_events = (
            db.query(Event)
            .filter(Event.end_date < datetime.utcnow())
            .count()
        )

        event_registrations = (
            db.query(
                Event.id,
                Event.event_name,
                func.count(Registration.id).label("registration_count")
            )
            .outerjoin(Registration, Registration.event_id == Event.id)
            .group_by(Event.id, Event.event_name)
            .all()
        )

        return {
            "total_events": total_events,
            "total_participants": total_participants,
            "upcoming_events": upcoming_events,
            "completed_events": completed_events,
            "event_wise_registrations": [
                {
                    "event_id": r.id,
                    "event_name": r.event_name,
                    "registration_count": r.registration_count
                }
                for r in event_registrations
            ]
        }