from pydantic import BaseModel, field_validator
from typing import List

class OrderItem(BaseModel):
    product_id: int
    quantity: int

class Order(BaseModel):
    items: List[OrderItem]
    total_amount: float

    @field_validator("total_amount")
    @classmethod
    def validate_total(cls, total, info):
        items = info.data.get("items", [])
        if not items:
            raise ValueError("Order must contain at least one item")
        if total <= 0:
            raise ValueError("Total amount must be positive")
        return total
