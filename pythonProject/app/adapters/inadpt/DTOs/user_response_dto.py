# DTO para la respuesta (excluyendo el password)
from typing import List

from pydantic import BaseModel


class UserResponseDTO(BaseModel):
    id: int
    user: str
    balance: float
    purchases: List[str]

    class Config:
        orm_mode = True  # Permite a Pydantic trabajar con objetos ORM o clases como `User`.
