from datetime import datetime

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.get_weather import get_weather_by_params
from app.check_city_and_country import check_city_and_country
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/weather", response_model=schemas.Weather)
def read_weather(country_code: str, city: str,
                 date_time: datetime,
                 db: Session = Depends(get_db)):

    check_city_and_country(city, country_code)

    db_weather = crud.get_weather_record(db, country_code=country_code,
                                         city=city, date_time=date_time)

    if db_weather is None:
        temperature = get_weather_by_params(city, country_code, date_time)
        return crud.add_weather_record(db, country_code=country_code,
                                       city=city, date_time=date_time,
                                       temperature=temperature)
    return db_weather
