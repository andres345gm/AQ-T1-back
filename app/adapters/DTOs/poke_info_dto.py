
from pydantic import BaseModel


class PokeInfoDTO(BaseModel):
    id: int
    name: str
    height: float
    weight: float
    hp: int
    attack: int
    image: str


def map_poke_to_dto(poke):
    return PokeInfoDTO(
        id=poke.id_,
        name=poke.name,
        height=poke.height,
        weight=poke.weight,
        hp=poke.hp,
        attack=poke.attack,
        image=poke.image
    )