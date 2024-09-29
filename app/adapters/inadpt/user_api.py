import logging

from fastapi import HTTPException, APIRouter

from app.adapters.DTOs.purchase_create_dto import PurchaseCreateDTO, map_dto_to_purchase
from app.adapters.DTOs.user_create_dto import UserCreateDTO
from app.adapters.DTOs.user_response_dto import UserResponseDTO, map_user_to_response_dto
from app.adapters.out.singleton import singletonUserRepository, singletonPurchaseRepository
from app.domain.model.user import User
from app.domain.services.add_purchase_service import AddPurchaseToUser
from app.domain.services.user_crud_service import UserCrudUseCase

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

user_router = APIRouter()

user_crud = UserCrudUseCase(singletonUserRepository)
add_purchases_use_case = AddPurchaseToUser(singletonUserRepository, singletonPurchaseRepository)

@user_router.post("/user", response_model=UserResponseDTO)
def create_user(user_data: UserCreateDTO):
    new_user = User(0, user_data.user, user_data.password)
    logger.info(f"Creating user: {new_user}")
    new_user = user_crud.create_user(user_data.user, user_data.password)
    if new_user:
        user_response = map_user_to_response_dto(new_user)
        return user_response
    raise HTTPException(status_code=404, detail="User not created")


@user_router.get("/user/{user_id}", response_model=UserResponseDTO)
def get_user(user_id: int): 
    user = user_crud.get_user(user_id)
    if user:
        user_response = map_user_to_response_dto(user)
        return user_response
    raise HTTPException(status_code=404, detail="User not found")


@user_router.put("/user/{user_id}", response_model=UserResponseDTO)
def update_user(user_id: int, user_data: UserCreateDTO):  # Cambiado a str para ObjectId
    updated_user = user_crud.update_user(user_id, user_data.user, user_data.password)
    if updated_user:
        user_response = map_user_to_response_dto(updated_user)
        return user_response
    raise HTTPException(status_code=404, detail="User not found")


@user_router.delete("/user/{user_id}")
def delete_user(user_id: int):  # Cambiado a str para ObjectId
    if user_crud.delete_user(user_id):
        return {"detail": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")


@user_router.post("/user/purchase", response_model=UserResponseDTO)
def add_purchase_to_user(purchase_data: PurchaseCreateDTO):  # Cambiado a str para ObjectId
    new_purchase = map_dto_to_purchase(purchase_data)
    logger.info(f"Adding purchase to user: {new_purchase.id_} - {new_purchase.id_user} - {new_purchase.price}")
    user = add_purchases_use_case.execute(new_purchase)
    if user:
        user_response = map_user_to_response_dto(user)
        return user_response

    raise HTTPException(status_code=404, detail="User not found")
