from datetime import datetime

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app import crud, models, schemas, open_weather_api
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
def get_temperature_info(country_code: str, city: str,
                         date_time: datetime,
                         db: Session = Depends(get_db)):

    db_weather = crud.get_weather_record(db, country_code=country_code,
                                         city=city, date_time=date_time)

    if db_weather is None:
        open_weather_api.validate_params(city, country_code)
        temperature = open_weather_api.get_temperature_by_params(city, country_code, date_time)
        return crud.add_weather_record(db, country_code=country_code,
                                       city=city, date_time=date_time,
                                       temperature=temperature)
    return db_weather
