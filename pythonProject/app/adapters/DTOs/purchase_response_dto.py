from pydantic import BaseModel

class PurchaseResponseDTO(BaseModel):
    id: int
    id_pokemon: int
    date: str
    price: int
    id_user: int

    class Config:
        arbitrary_types_allowed = True  # Allows arbitrary types like your custom models
        from_attributes = True  # Enables loading data from ORM models
