from pydantic import BaseModel

from app.domain.model.purchase import Purchase


class PurchaseResponseDTO(BaseModel):
    id: int
    id_pokemon: int
    date: str
    price: int
    id_user: int

    class Config:
        arbitrary_types_allowed = True  # Allows arbitrary types like your custom models
        from_attributes = True  # Enables loading data from ORM models


def map_purchase_to_dto(purchase: Purchase) -> PurchaseResponseDTO:
    return PurchaseResponseDTO(
        id=purchase.id_,  # Mapping the correct attribute
        id_pokemon=purchase.id_pokemon,
        date=purchase.date,
        price=purchase.price,
        id_user=purchase.id_user
    )
