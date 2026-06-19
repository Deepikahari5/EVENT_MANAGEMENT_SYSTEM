from pydantic import BaseModel, EmailStr, Field


class RegisterSchema(BaseModel):
    full_name: str
    email: EmailStr
    password: str = Field(
        min_length=6,
        max_length=72
    )


class LoginSchema(BaseModel):
    email: EmailStr
    password: str
class LoginSchema(BaseModel):
    email: EmailStr
    password: str