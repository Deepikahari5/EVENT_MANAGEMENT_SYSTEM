from sqlalchemy import asc, desc
from app.models.registration import Registration


class RegistrationRepository:

    @staticmethod
    def create(db, registration):
        db.add(registration)
        db.commit()
        db.refresh(registration)
        return registration

    @staticmethod
    def get_all(db):
        return db.query(Registration).all()

    @staticmethod
    def get_by_id(db, registration_id):
        return (
            db.query(Registration)
            .filter(Registration.id == registration_id)
            .first()
        )

    @staticmethod
    def delete(db, registration):
        db.delete(registration)
        db.commit()

    @staticmethod
    def search(
        db,
        event_id=None,
        user_id=None,
        page=1,
        size=10,
        sort_by="id",
        order="asc"
    ):
        query = db.query(Registration)

        if event_id:
            query = query.filter(
                Registration.event_id == event_id
            )

        if user_id:
            query = query.filter(
                Registration.user_id == user_id
            )

        sort_column = getattr(
            Registration,
            sort_by,
            Registration.id
        )

        if order.lower() == "desc":
            query = query.order_by(
                desc(sort_column)
            )
        else:
            query = query.order_by(
                asc(sort_column)
            )

        offset = (page - 1) * size

        return (
            query
            .offset(offset)
            .limit(size)
            .all()
        )