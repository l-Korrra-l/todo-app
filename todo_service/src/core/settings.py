from typing import Any, Dict, Optional

from pydantic import BaseSettings, PostgresDsn, validator


class CustomPostgresDsn(PostgresDsn):
    allowed_schemes = {"postgres", "postgresql", "postgresql+asyncpg"}


class SettingsPostgres(BaseSettings):
    POSTGRES_HOST: Optional[str]
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    SQLALCHEMY_DATABASE_URI: Optional[CustomPostgresDsn] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v

        return CustomPostgresDsn.build(
            scheme="postgresql+asyncpg",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_HOST")
            if values.get("POSTGRES_HOST")
            else "127.0.0.1",
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    class Config:
        case_sensitive = True
        env_file = ".env"

class SettingsJWT(BaseSettings):
    JWT_REFRESH_SECRET_KEY: str
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    JWT_EXP_MIN: int = 180
    JWT_REFRESH_EXP_MIN: int = 720

    @validator("JWT_ALGORITHM", pre=True)
    def validate_algorithm(cls, v: str, values: Dict[str, Any]) -> Optional[str]:
        available_algorithms = [
            "HS256",
            "HS384",
            "HS512",
            "ES256",
            "ES384",
            "ES512",
            "RS256",
            "RS384",
            "RS512",
            "PS256",
            "PS384",
            "PS512",
            "EdDSA",
            "ES256K",
        ]
        if v in available_algorithms:
            return v
        raise ValueError("Algorithm can not be found.")

    class Config:
        case_sensitive = True
        env_file = ".env"

