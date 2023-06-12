import re
from typing import Optional

from pydantic import BaseModel, validator


class PasswordBaseSchema(BaseModel):
    password: str

    @validator("password")
    def validate_password(cls, value):
        """4-15 sym: one lowercase letter, one uppercase letter and one digit"""
        if re.match(r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{4,15}", value):
            return value
        raise ValueError("Password doesn't match requirements")


class EmailBaseSchema(BaseModel):
    email: str

    @validator("email")
    def validate_email(cls, value):
        if re.match(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+", value):
            return value
        raise ValueError("Email does not satisfy requirements.")

    @validator("email")
    def validate_email_len(cls, value):
        len_ = len(value)
        if len_ < 2 or len_ > 50:
            raise ValueError("Min length of email is 2. Max length of email is 50")
        return value


class UserCreateSchema(PasswordBaseSchema, EmailBaseSchema):
    first_name: str
    last_name: str
    phone: str

    @validator("phone")
    def validate_phone(cls, value):
        if re.match(r"^(\+)[1-9][0-9\-\(\)\.]{8,15}$", value):
            return value
        raise ValueError("Phone doesn't match requirements")

    @validator("last_name")
    def validate_full_name(cls, value, values, **kwargs):
        first_name = values.get("first_name") if values.get("first_name") else ""
        if len(value) + len(first_name) > 40:
            raise ValueError("FullName more than 40 sym")
        return value

    class Config:
        orm_mode = True


class UserUpdateSchema(UserCreateSchema):
    email: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    phone: Optional[str]
    password: Optional[str]


class UserLoginSchema(PasswordBaseSchema, EmailBaseSchema):
    pass


class GetUserSchema(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    phone: str

    class Config:
        orm_mode = True
