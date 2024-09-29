from pydantic import BaseModel

from app.domain.model.purchase import Purchase


class PurchaseCreateDTO(BaseModel):
    id_pokemon: int
    date: str
    price: int
    id_user: int


def map_dto_to_purchase(purchase_data: PurchaseCreateDTO):
    purchase = Purchase(
        id=0,
        id_pokemon=purchase_data.id_pokemon,
        date=purchase_data.date,
        price=purchase_data.price,
        id_user=purchase_data.id_user
    )
    return purchase
