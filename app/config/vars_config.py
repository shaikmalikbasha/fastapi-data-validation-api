from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str
    ADMIN_MAIL: str
    DEVELOPER_GITHUB_LINK: str
    SQLALCHEMY_DATABASE_URI: str

    class Config:
        env_file = ".env"


settings = Settings()
