from pydantic import BaseModel


class PokeMiniInfoDTO(BaseModel):
    id: int
    name: str
    image: str