from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Awesome API"
    ADMIN_EMAIL: str
    SQLALCHEMY_DATABASE_URI: str

    class Config:
        env_file = ".env"


settings = Settings()
