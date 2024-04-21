from sqlalchemy import Column, Integer, String, Float

from config.database import Base


class Restaurant(Base):
    __tablename__ = 'Restaurant'

    id = Column(String, primary_key=True)
    rating = Column(Integer)
    name = Column(String)
    site = Column(String)
    email = Column(String)
    phone = Column(String)
    street = Column(String)
    city = Column(String)
    state = Column(String)
    lat = Column(Float)
    lng = Column(Float)
