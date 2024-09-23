# DTO para la respuesta (excluyendo el password)
from typing import List

from pydantic import BaseModel

from pythonProject.app.adapters.DTOs.purchase_response_dto import PurchaseResponseDTO
from pythonProject.app.domain.model.purchase import Purchase


class UserResponseDTO(BaseModel):
    id: int
    user: str
    balance: int
    purchases: List[PurchaseResponseDTO]

    model_config = {
        "arbitrary_types_allowed": True,  # Allows arbitrary types like your custom models
        "from_attributes": True,  # Replaces 'orm_mode'
    }