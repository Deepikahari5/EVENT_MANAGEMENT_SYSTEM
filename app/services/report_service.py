from sqlalchemy import func
from app.models.event import Event
from app.models.registration import Registration
from app.models.attendance import Attendance
from app.models.user import User


class ReportService:

    @staticmethod
    def event_report(db):
        results = (
            db.query(
                Event.id,
                Event.event_name,
                Event.venue,
                Event.start_date,
                Event.capacity,
                func.count(Registration.id).label("registrations")
            )
            .outerjoin(Registration, Registration.event_id == Event.id)
            .group_by(Event.id, Event.event_name, Event.venue, Event.start_date, Event.capacity)
            .all()
        )
        return [
            {
                "event_id": r.id,
                "event_name": r.event_name,
                "venue": r.venue,
                "start_date": str(r.start_date),
                "capacity": r.capacity,
                "registrations": r.registrations
            }
            for r in results
        ]

    @staticmethod
    def attendance_report(db):
        results = (
            db.query(
                Event.id,
                Event.event_name,
                func.count(Attendance.id).label("attendance_count")
            )
            .outerjoin(Attendance, Attendance.event_id == Event.id)
            .group_by(Event.id, Event.event_name)
            .all()
        )
        return [
            {
                "event_id": r.id,
                "event_name": r.event_name,
                "attendance_count": r.attendance_count
            }
            for r in results
        ]

    @staticmethod
    def registration_report(db):
        results = (
            db.query(
                Event.id,
                Event.event_name,
                func.count(Registration.id).label("total"),
                func.sum(
                    func.IF(Registration.status == "Registered", 1, 0)
                ).label("active"),
                func.sum(
                    func.IF(Registration.status == "Cancelled", 1, 0)
                ).label("cancelled")
            )
            .outerjoin(Registration, Registration.event_id == Event.id)
            .group_by(Event.id, Event.event_name)
            .all()
        )
        return [
            {
                "event_id": r.id,
                "event_name": r.event_name,
                "total_registrations": r.total,
                "active": r.active or 0,
                "cancelled": r.cancelled or 0
            }
            for r in results
        ]