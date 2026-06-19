from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.user import User
from app.core.security import decode_token

bearer_scheme = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
    db: Session = Depends(get_db)
):
    token = credentials.credentials
    print("TOKEN:", token)

    payload = decode_token(token)
    print("PAYLOAD:", payload)

    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )

    user_id = payload.get("user_id")
    print("USER_ID:", user_id)

    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token missing user_id"
        )

    user = db.query(User).filter(User.id == user_id).first()
    print("USER:", user)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user