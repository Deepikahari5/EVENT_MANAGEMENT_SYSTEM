from fastapi import HTTPException
from app.models.attendance import Attendance
from app.repositories.ticket_repo import TicketRepository
from app.repositories.attendance_repo import AttendanceRepository


class AttendanceService:

    @staticmethod
    def mark_attendance(db, ticket_id):

        ticket = TicketRepository.get_by_id(db, ticket_id)

        if not ticket:
            raise HTTPException(status_code=404, detail="Ticket not found")

        if ticket.status != "Active":
            raise HTTPException(status_code=400, detail="Ticket is not active")

        registration = ticket.registration

        existing = AttendanceRepository.get_existing(
            db, registration.event_id, registration.user_id
        )
        if existing:
            raise HTTPException(status_code=400, detail="Attendance already marked")

        attendance = Attendance(
            event_id=registration.event_id,
            user_id=registration.user_id,
            status="Present"
        )

        return AttendanceRepository.create(db, attendance)

    @staticmethod
    def get_event_attendance(db, event_id):
        return AttendanceRepository.get_by_event(db, event_id)

    @staticmethod
    def summary(db, event_id):
        total = AttendanceRepository.count_by_event(db, event_id)
        return {"event_id": event_id, "total_attendance": total}