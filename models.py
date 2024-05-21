from .db import Base
from sqlalchemy import Column, Integer, String


class Car(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True, nullable=False)
    car_model = Column(String, nullable=False)
    car_cost = Column(String, nullable=False)