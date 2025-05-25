from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from app.models import Offer, Meal
from app.schemas import OfferCreate
from typing import Optional, List

class OfferService():

    async def createOffer(self, offer: OfferCreate, db: AsyncSession):
        meals = []
        for meal in offer.meals:
            db_meal = Meal(
                meal_code=meal.meal_code,
                name=meal.name,
                description=meal.description,
                notes=meal.notes,
                quantity=meal.quantity
            )
            db.add(db_meal)
            await db.flush()
            meals.append(db_meal)

        db_offer = Offer(
            name=offer.name,
            duration=offer.duration,
            price=offer.price,
            price_id=offer.price_id,
            product_id=offer.product_id,
            kitchen_id=offer.kitchen_id,
            meals=meals
        )

        db.add(db_offer)
        await db.commit()
        await db.refresh(db_offer)

        return db_offer


    async def get_all_offers(self, db: AsyncSession):
        result = await db.execute(
            select(Offer).options(joinedload(Offer.meals))
        )
        offers = result.scalars().unique().all()
        return offers
    
    
    async def get_offer_by_id(self, db: AsyncSession, offer_id: int) -> Optional[Offer]:
        result = await db.execute(
            select(Offer)
            .options(joinedload(Offer.meals))
            .where(Offer.id == offer_id)
        )
        offer = result.scalars().unique().first()
        return offer
    

    async def get_offers_by_ids(self, db: AsyncSession, offer_ids: List[int]) -> List[Offer]:
        if not offer_ids:
            return []

        result = await db.execute(
            select(Offer)
            .options(joinedload(Offer.meals))  # Optional: eager load meals
            .where(Offer.id.in_(offer_ids))
        )
        offers = result.scalars().unique().all()
        return offers