from app.models.user import UserBase

class UserCreateRequest(UserBase):
    password: str

    @classmethod
    def validate_password_strength(cls, value: str):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")
        return value
