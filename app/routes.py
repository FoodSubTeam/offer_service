from fastapi import APIRouter, Query
from app.schemas import OfferCreate, OfferSelect, OfferRead, OfferIdsRequest
from app.service import OfferService
from app.database import SessionLocal
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.kafka import KafkaProducerSingleton
from typing import List

router = APIRouter()
offerService = OfferService()

async def get_db():
    async with SessionLocal() as session:
        yield session


# Creates a new offer
@router.post("/offer")
async def create_offer(offer: OfferCreate, db: AsyncSession = Depends(get_db)):
    db_offer = await offerService.createOffer(offer, db)
    return {"message": "Offer created successfully!"}


# Returns all offers
@router.get("/offers")
async def get_all_offers(db: AsyncSession = Depends(get_db)):
    offers = await offerService.get_all_offers(db)
    return {"offers": offers}


# Returns the offer with the given id
@router.get("/offer/{offer_id}", response_model=OfferRead)
async def get_offer_by_id(offer_id: int, db: AsyncSession = Depends(get_db)):
    offer = await offerService.get_offer_by_id(db, offer_id)
    if not offer:
        raise HTTPException(status_code=404, detail="Offer not found")
    return offer


# Returns all the offers with given ids
@router.post("/offers-by-ids", response_model=List[OfferRead])
async def get_offers_by_ids(
    request: OfferIdsRequest,
    db: AsyncSession = Depends(get_db)
):
    offers = await offerService.get_offers_by_ids(db, request.offer_ids)
    if not offers:
        raise HTTPException(status_code=404, detail="No offers found")
    return offers