from pydantic_settings import BaseSettings


class DBSettings(BaseSettings):
    REDIS_HOST: str
    REDIS_PORT: str
    REDIS_SECRET_KEY: str

    class Config:
        env_file = "../.env"


redis_settings = DBSettings()
