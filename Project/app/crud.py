from sqlalchemy.orm import Session
from datetime import datetime

from app import models, schemas


def get_temp(db: Session, country_code: str, city: str,
             date_time: datetime):
    return db.query(models.Weather).filter(
        models.Weather.country_code == country_code,
        models.Weather.city == city,
        models.Weather.date_time == date_time
    ).first()


def add_temp(db: Session, country_code: str, city: str,
             date_time: datetime, temp: None):
    db_weather = models.Weather(country_code=country_code, city=city,
                                date_time=date_time, temp=temp)
    db.add(db_weather)
    db.commit()
    db.refresh(db_weather)
    return db_weather
