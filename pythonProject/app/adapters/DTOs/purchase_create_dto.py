from pydantic import BaseModel

class PurchaseCreateDTO(BaseModel):
    id_pokemon: int
    date: str
    price: int
    id_user: int