from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    github_client_id: str = Field(env="GITHUB_CLIENT_ID")
    github_client_secret: str = Field(env="GITHUB_CLIENT_SECRET")
    app_secret_key: str = Field(env="APP_SECRET_KEY")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()  # type: ignore
