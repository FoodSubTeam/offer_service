from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class MealCreate(BaseModel):
    name: str
    description: str

class OfferCreate(BaseModel):
    name: str
    duration: int
    pricePerDay: float
    meals: List[MealCreate]

    class Config:
        orm_mode = True 