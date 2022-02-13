from sqlalchemy import Float, Column, String, Integer, DateTime

from app.database import Base


class Weather(Base):
    __tablename__ = "temp_info"

    country_code = Column(String, primary_key=True)
    city = Column(String, primary_key=True)
    date_time = Column(DateTime, primary_key=True)
    temp = Column(Float)
