
from pydantic import BaseModel


class PokeInfoDTO(BaseModel):
    id: int
    name: str
    height: float
    weight: float
    hp: int
    attack: int
    image: str