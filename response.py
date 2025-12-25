from app.models.base import BaseSchema
from app.models.user import Address

class UserResponse(BaseSchema):
    email: str
    full_name: str
    age: int
    address: Address
