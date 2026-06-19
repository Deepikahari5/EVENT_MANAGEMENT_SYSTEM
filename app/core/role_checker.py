from fastapi import HTTPException
from fastapi import status
from fastapi import Depends

from app.core.dependencies import get_current_user


class RoleChecker:

    def __init__(self, allowed_roles: list):
        self.allowed_roles = allowed_roles

    def __call__(
        self,
        current_user=Depends(get_current_user)
    ):
        print("USER EMAIL:", current_user.email)
        print("ROLE NAME:", current_user.role.name)
        print("ALLOWED:", self.allowed_roles)

        if current_user.role.name not in self.allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Permission denied. Your role '{current_user.role.name}' is not in {self.allowed_roles}"
            )

        return current_user