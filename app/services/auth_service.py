from fastapi import HTTPException
from app.models.user import User
from app.models.role import Role
from app.repositories.auth_repo import AuthRepository
from app.core.security import get_password_hash, verify_password, create_access_token


class AuthService:

    @staticmethod
    def register(db, user_data):

        existing_user = AuthRepository.get_user_by_email(
            db,
            user_data.email
        )

        if existing_user:
            raise HTTPException(
                status_code=400,
                detail="Email already registered"
            )

        default_role = db.query(Role).filter(
            Role.name == "Participant"
        ).first()

        if not default_role:
            raise HTTPException(
                status_code=500,
                detail="Default role 'Participant' not found in database"
            )

        user = User(
            full_name=user_data.full_name,
            email=user_data.email,
            password_hash=get_password_hash(user_data.password),
            role_id=default_role.id
        )

        return AuthRepository.create_user(db, user)

    @staticmethod
    def login(db, user_data):

        user = AuthRepository.get_user_by_email(
            db,
            user_data.email
        )

        if not user:
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password"
            )

        if not verify_password(user_data.password, user.password_hash):
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password"
            )

        if not user.is_active:
            raise HTTPException(
                status_code=403,
                detail="Account is inactive"
            )

        access_token = create_access_token(
            data={"user_id": user.id}
        )

        return {
            "access_token": access_token,
            "token_type": "bearer",
            "user": {
                "id": user.id,
                "full_name": user.full_name,
                "email": user.email,
                "role_id": user.role_id
            }
        }