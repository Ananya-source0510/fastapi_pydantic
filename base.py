from pydantic import BaseModel, Field
from datetime import datetime

class BaseSchema(BaseModel):
    id: int = Field(..., gt=0)
    created_at: datetime

    class Config:
        orm_mode = True
