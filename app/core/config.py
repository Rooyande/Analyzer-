# app/core/config.py
import os
from dataclasses import dataclass
from dotenv import load_dotenv

from .constants import DEFAULT_TIMEZONE, DEFAULT_REPORT_HOUR, DEFAULT_REPORT_MINUTE

load_dotenv()


@dataclass(frozen=True)
class Settings:
    # Telegram
    TG_BOT_TOKEN: str
    OWNER_USER_ID: int

    # Database
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str

    # General
    DEFAULT_TZ: str
    REPORT_HOUR: int
    REPORT_MINUTE: int
    ENV: str


def _require(name: str) -> str:
    v = os.getenv(name)
    if not v:
        raise RuntimeError(f"Missing required env var: {name}")
    return v


def load_settings() -> Settings:
    tg_token = _require("TG_BOT_TOKEN")
    owner_id = int(_require("OWNER_USER_ID"))

    db_host = os.getenv("DB_HOST", "db")
    db_port = int(os.getenv("DB_PORT", "5432"))
    db_name = os.getenv("DB_NAME", "tgstats")
    db_user = os.getenv("DB_USER", "tgstats")
    db_password = _require("DB_PASSWORD")

    default_tz = os.getenv("DEFAULT_TZ", DEFAULT_TIMEZONE)

    report_hour = int(os.getenv("REPORT_HOUR", str(DEFAULT_REPORT_HOUR)))
    report_minute = int(os.getenv("REPORT_MINUTE", str(DEFAULT_REPORT_MINUTE)))

    env = os.getenv("ENV", "prod")

    return Settings(
        TG_BOT_TOKEN=tg_token,
        OWNER_USER_ID=owner_id,
        DB_HOST=db_host,
        DB_PORT=db_port,
        DB_NAME=db_name,
        DB_USER=db_user,
        DB_PASSWORD=db_password,
        DEFAULT_TZ=default_tz,
        REPORT_HOUR=report_hour,
        REPORT_MINUTE=report_minute,
        ENV=env,
    )

