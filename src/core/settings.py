from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).parent.parent


class PostgresSettings(BaseModel):
    user: str = ""
    password: str = ""
    db: str = ""
    host: str = ""
    port: str = ""

    @property
    def dsn(self) -> str:
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}"


class BotSettings(BaseModel):
    token: str = ""


class Settings(BaseSettings):
    model_config: SettingsConfigDict = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP__",
    )
    bot: BotSettings = BotSettings()
    postgres: PostgresSettings = PostgresSettings()


settings = Settings()
