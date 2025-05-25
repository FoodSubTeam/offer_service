from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
import os
from app.models import Base

database_url = os.getenv("DATABASE_URL")

# DATABASE_URL = "postgresql+asyncpg://myuser:mypassword@postgres:5432/offer_db"

engine = create_async_engine(database_url, echo=True)
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)