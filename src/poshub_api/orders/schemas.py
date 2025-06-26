from annotated_types import Gt
from typing_extensions import TypeAliasType

from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, Field


PositiveIntList = TypeAliasType('PositiveIntList', list[Annotated[int, Gt(0)]])

class OrderIn(BaseModel):
    order_id: str = Field(..., alias="orderId")
    created_at: datetime = Field(..., alias="createdAt")
    total_amount: float = Field(..., alias="totalAmount", gt=0)
    currency: str = Field(..., alias="currency")

class OrderOut(BaseModel):
    order_id: str = Field(..., alias="orderId")
    created_at: datetime = Field(..., alias="createdAt")
    total_amount: float = Field(..., alias="totalAmount", gt=0)
    currency: str = Field(..., alias="currency")