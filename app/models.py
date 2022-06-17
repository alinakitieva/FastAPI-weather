from sqlalchemy import Float, Column, String, Integer, DateTime, UniqueConstraint

from app.database import Base


class Weather(Base):
    __tablename__ = "weathers"

    id = Column(Integer, primary_key=True, index=True)
    country_code = Column(String)
    city = Column(String)
    date_time = Column(DateTime)
    temperature = Column(Float)

    UniqueConstraint('country_code', 'city', 'date_time', name='wheather_unique_field_1')
