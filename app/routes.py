from fastapi import APIRouter
from app.schemas import OfferCreate
from app.service import OfferService
from app.database import SessionLocal
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

router = APIRouter()
offerService = OfferService()

async def get_db():
    async with SessionLocal() as session:
        yield session

@router.post("/offer/create-offer/")
async def create_offer(offer: OfferCreate, db: AsyncSession = Depends(get_db)):
    await offerService.createOffer(offer, db)
    return {"message": "Offer created successfully!"}

@router.get("/offer/offers/")
async def get_all_offers(db: AsyncSession = Depends(get_db)):
    offers = await offerService.get_all_offers(db)
    return {"offers": offers}