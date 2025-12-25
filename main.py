from fastapi import FastAPI
from app.schemas.request import UserCreateRequest
from app.schemas.response import UserResponse
from datetime import datetime

app = FastAPI(title="FastAPI Pydantic Validation Demo")

@app.post("/users", response_model=UserResponse)
def create_user(user: UserCreateRequest):
    return {
        "id": 1,
        "email": user.email,
        "full_name": user.full_name,
        "age": user.age,
        "address": user.address,
        "created_at": datetime.utcnow()
    }
