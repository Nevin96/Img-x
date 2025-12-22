from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME : str
    SECRET_KEY : str
    ACCESS_TOKEN_EXPIRE_MINUTES : int
    REFRESH_TOKEN_EXPIRE_DAYS : int
    DATABASE_URL : str

    class Config:
        env_file = '.env'
        case_sensitive = True

settings = Settings()


