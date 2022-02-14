from pydantic import BaseSettings


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str = "postgresql://postgres:password@db:5432/apidb"
    appid: str = 'e8254b56019f6c404ceecd4e5415e511'


settings = Settings()
