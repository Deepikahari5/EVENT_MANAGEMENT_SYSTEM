from sqlalchemy.orm import Session

from app.models.attendance import Attendance


class AttendanceRepository:

    @staticmethod
    def create(
        db: Session,
        attendance
    ):
        db.add(attendance)
        db.commit()
        db.refresh(attendance)

        return attendance

    @staticmethod
    def get_existing(
        db: Session,
        event_id: int,
        user_id: int
    ):
        return (
            db.query(Attendance)
            .filter(
                Attendance.event_id == event_id,
                Attendance.user_id == user_id
            )
            .first()
        )

    @staticmethod
    def get_by_event(
        db: Session,
        event_id: int
    ):
        return (
            db.query(Attendance)
            .filter(
                Attendance.event_id == event_id
            )
            .all()
        )

    @staticmethod
    def count_by_event(
        db: Session,
        event_id: int
    ):
        return (
            db.query(Attendance)
            .filter(
                Attendance.event_id == event_id
            )
            .count()
        )