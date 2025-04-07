from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from app.models import Offer, Meal
from app.schemas import OfferCreate

class OfferService():

    async def createOffer(self, offer: OfferCreate, db: AsyncSession):
        meals = []
        for meal in offer.meals:
            db_meal = Meal(
                name= meal.name,
                description = meal.description
            )
            meals.append(db_meal)
        db_offer = Offer(
            name=offer.name,
            duration=offer.duration,
            pricePerDay=offer.pricePerDay,
            meals=meals
        )
        db.add(db_offer)
        await db.commit()

    async def get_all_offers(self, db: AsyncSession):
        result = await db.execute(
            select(Offer).options(joinedload(Offer.meals))
        )
        offers = result.scalars().unique().all()
        return offers