from app.models.audit_log import AuditLog


class AuditRepository:

    @staticmethod
    def create(
        db,
        user_id,
        action,
        entity,
        description
    ):

        log = AuditLog(
            user_id=user_id,
            action=action,
            entity=entity,
            description=description
        )

        db.add(log)
        db.commit()

        return log