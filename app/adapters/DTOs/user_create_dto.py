# DTO para la creación de usuarios (incluyendo el password)
from pydantic import BaseModel


class UserCreateDTO(BaseModel):
    user: str
    password: str



