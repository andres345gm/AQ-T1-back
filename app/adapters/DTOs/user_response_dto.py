# DTO para la respuesta (excluyendo el password)
from typing import List

from pydantic import BaseModel

from app.adapters.DTOs.purchase_response_dto import PurchaseResponseDTO, map_purchase_to_dto
from app.domain.model.user import User


class UserResponseDTO(BaseModel):
    id: int
    user: str
    balance: int
    purchases: List[PurchaseResponseDTO]

    model_config = {
        "arbitrary_types_allowed": True,  # Allows arbitrary types like your custom models
        "from_attributes": True,  # Replaces 'orm_mode'
    }


def map_user_to_response_dto(user: 'User') -> UserResponseDTO:
    # Map each purchase in the user object to a PurchaseResponseDTO
    purchases_dto = [
        map_purchase_to_dto(purchase)  # Call the function to map the purchase to a DTO
        for purchase in user.purchases
    ]

    # Return the UserResponseDTO, populating the fields from the user object
    return UserResponseDTO(
        id=user.id_,
        user=user.user,
        balance=user.balance,
        purchases=purchases_dto
    )

