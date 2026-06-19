from fastapi import HTTPException
from app.models.registration import Registration
from app.repositories.registration_repo import RegistrationRepository
from app.repositories.event_repo import EventRepository


class RegistrationService:

    @staticmethod
    def register(db, event_id, current_user):

        event = EventRepository.get_by_id(db, event_id)

        if not event:
            raise HTTPException(status_code=404, detail="Event not found")

        existing = RegistrationRepository.search(
            db, event_id=event_id, user_id=current_user.id
        )
        if existing:
            raise HTTPException(status_code=400, detail="Already registered for this event")

        total_registered = len(
            RegistrationRepository.search(db, event_id=event_id, size=10000)
        )
        if total_registered >= event.capacity:
            raise HTTPException(status_code=400, detail="Event is at full capacity")

        registration = Registration(
            user_id=current_user.id,
            event_id=event_id,
            status="Registered"
        )

        return RegistrationRepository.create(db, registration)

    @staticmethod
    def my_registrations(db, current_user):
        return RegistrationRepository.search(
            db, user_id=current_user.id, size=1000
        )

    @staticmethod
    def cancel(db, registration_id, current_user):

        registration = RegistrationRepository.get_by_id(db, registration_id)

        if not registration:
            raise HTTPException(status_code=404, detail="Registration not found")

        if registration.user_id != current_user.id:
            raise HTTPException(status_code=403, detail="Not your registration")

        if registration.status == "Cancelled":
            raise HTTPException(status_code=400, detail="Already cancelled")

        registration.status = "Cancelled"
        db.commit()
        db.refresh(registration)

        return registration