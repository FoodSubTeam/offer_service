from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

offer_meal_table = Table(
    "offer_meal", Base.metadata,
    Column("offer_id", Integer, ForeignKey("offers.id"), primary_key=True),
    Column("meal_id", Integer, ForeignKey("meals.id"), primary_key=True)
)

class Offer(Base):
    __tablename__ = "offers"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    duration = Column(Integer)  # days
    pricePerDay = Column(Float)
    meals = relationship("Meal", secondary=offer_meal_table, cascade="all, delete")


class Meal(Base):
    __tablename__ = "meals"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    description = Column(String)