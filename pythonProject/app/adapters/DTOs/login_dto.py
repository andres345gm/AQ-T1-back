from pydantic import BaseModel


class LoginDTO(BaseModel):
    user: str
    password: str