from datetime import datetime
from pydantic import BaseModel, Field

class OrderIn(BaseModel):
    order_id: str = Field(..., alias="orderId")
    created_at: datetime = Field(..., alias="createdAt")
    total_amount: float = Field(..., alias="totalAmount", g=0)
    currency: str = Field(..., alias="currency")

class OrderOut(BaseModel):
    order_id: str = Field(..., alias="orderId")
    created_at: datetime = Field(..., alias="createdAt")
    total_amount: float = Field(..., alias="totalAmount", g=0)
    currency: str = Field(..., alias="currency")