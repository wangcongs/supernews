from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "news_platform"
    VERSION: str = "0.1.0"
    DATABASE_URL: str = "mysql+aiomysql://root:mysql@localhost/news_app?charset=utf8mb4"

    class Config:
        env_file = ".env"


settings = Settings()
