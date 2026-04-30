from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    anthropic_api_key: str
    claude_model: str = "claude-sonnet-4-6"
    output_dir: str = "./outputs"
    max_retries: int = 2
    cors_origins: list[str] = ["http://localhost:3000"]
    log_level: str = "INFO"


settings = Settings()
