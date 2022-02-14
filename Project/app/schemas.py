from pydantic import BaseModel
from datetime import datetime


class WeatherBase(BaseModel):
    country_code: str
    city: str
    date_time: datetime


class WeatherCreate(WeatherBase):
    pass


class Weather(WeatherBase):
    temperature: float

    class Config:
        orm_mode = True
