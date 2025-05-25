from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class MealCreate(BaseModel):
    meal_code: str
    name: str
    description: str
    notes: Optional[str] = None
    quantity: int


class OfferCreate(BaseModel):
    name: str
    duration: int
    price: float
    price_id: str
    product_id: str
    kitchen_id: int
    meals: List[MealCreate]

    class Config:
        orm_mode = True


class OfferSelect(BaseModel):
    user_id: int
    offer_id: int


# Read
class MealRead(BaseModel):
    id: int
    meal_code: Optional[str]
    name: str
    description: str
    notes: Optional[str]
    quantity: Optional[int]

    class Config:
        orm_mode = True

class OfferRead(BaseModel):
    id: int
    name: str
    duration: int
    price: float
    price_id: str
    product_id: str
    kitchen_id: int
    meals: List[MealRead]

    class Config:
        orm_mode = True

class OfferIdsRequest(BaseModel):
    offer_ids: List[int]