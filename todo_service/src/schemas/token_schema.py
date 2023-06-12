from pydantic import BaseModel


class TokenSchema(BaseModel):
    token: str


class LoginTokens(BaseModel):
    access_token: str
    refresh_token: str
