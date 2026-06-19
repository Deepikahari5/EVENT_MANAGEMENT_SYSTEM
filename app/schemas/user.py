
from pydantic import BaseModel, EmailStr
from datetime import datetime

class AdminCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    role_id: int
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True