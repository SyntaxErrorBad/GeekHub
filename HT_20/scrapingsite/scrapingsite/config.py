from pydantic_settings import BaseSettings


class DBSettings(BaseSettings):
    REDIS_HOST: str
    REDIS_PORT: str

    class Config:
        env_file = "../.env"


redis_settings = DBSettings()
