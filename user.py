from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional

class Address(BaseModel):
    street: str
    city: str
    country: str

class UserBase(BaseModel):
    email: EmailStr
    full_name: str
    age: int
    address: Address

    @field_validator("age")
    @classmethod
    def validate_age(cls, value):
        if value < 18:
            raise ValueError("User must be at least 18 years old")
        return value
