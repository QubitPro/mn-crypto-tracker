"""Application configuration."""
import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    """Global settings loaded from environment."""

    APP_NAME: str = "MN Crypto Tracker"
    VERSION: str = "0.1.0"
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"

    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///data/crypto.db")

    # External APIs
    COINGECKO_BASE_URL: str = "https://api.coingecko.com/api/v3"
    PRICE_UPDATE_INTERVAL: int = 30  # seconds

    # Server
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))


settings = Settings()