from app.repositories.audit_repo import (
    AuditRepository
)


class AuditService:

    @staticmethod
    def log(
        db,
        user_id,
        action,
        entity,
        description
    ):
        AuditRepository.create(
            db,
            user_id,
            action,
            entity,
            description
        )