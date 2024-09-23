from pydantic import BaseModel

class PurchaseResponseDTO(BaseModel):
    id: int
    id_pokemon: int
    date: str
    price: int
    id_user: int

    class Config:
        orm_mode = True