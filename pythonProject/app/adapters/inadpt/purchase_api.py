from typing import List

from fastapi import HTTPException, APIRouter

from pythonProject.app.adapters.DTOs.purchase_create_dto import PurchaseCreateDTO
from pythonProject.app.adapters.DTOs.purchase_response_dto import PurchaseResponseDTO
from pythonProject.app.adapters.out.mock_purchase_repository import MockPurchaseRepository
from pythonProject.app.domain.use_cases.purchase_crud_use_case import PurchaseCrudUseCase

purchase_router = APIRouter()

purchase_repo = MockPurchaseRepository()
purchase_crud = PurchaseCrudUseCase(purchase_repo)

@purchase_router.post("/purchase", response_model=PurchaseResponseDTO)
def create_purchase(purchase_data: PurchaseCreateDTO):
    new_purchase = purchase_crud.create_purchase(purchase_data.id_pokemon, purchase_data.date, purchase_data.price, purchase_data.id_user)
    return new_purchase

@purchase_router.get("/purchase/{purchase_id}", response_model=PurchaseResponseDTO)
def get_purchase(purchase_id: int):
    purchase = purchase_crud.get_purchase(purchase_id)
    if purchase:
        return purchase
    raise HTTPException(status_code=404, detail="Purchase not found")

@purchase_router.put("/purchase/{purchase_id}", response_model=PurchaseResponseDTO)
def update_purchase(purchase_id: int, purchase_data: PurchaseCreateDTO):
    updated_purchase = purchase_crud.update_purchase(purchase_id, purchase_data.id_pokemon, purchase_data.date, purchase_data.price, purchase_data.id_user)
    if updated_purchase:
        return updated_purchase
    raise HTTPException(status_code=404, detail="Purchase not found")

@purchase_router.delete("/purchase/{purchase_id}")
def delete_purchase(purchase_id: int):
    if purchase_crud.delete_purchase(purchase_id):
        return {"detail": "Purchase deleted"}
    raise HTTPException(status_code=404, detail="Purchase not found")

@purchase_router.get("/purchase", response_model=List[PurchaseResponseDTO])
def list_purchases():
    return purchase_crud.list_purchases()

@purchase_router.get("/purchase/user/{user_id}", response_model=List[PurchaseResponseDTO])
def list_purchases_user(user_id: int):
    return purchase_crud.list_purchases_user(user_id)
