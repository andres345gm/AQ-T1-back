import logging
from typing import List

from fastapi import HTTPException, APIRouter

from pythonProject.app.adapters.DTOs.purchase_response_dto import PurchaseResponseDTO
from pythonProject.app.adapters.DTOs.user_create_dto import UserCreateDTO
from pythonProject.app.adapters.DTOs.user_response_dto import UserResponseDTO
from pythonProject.app.adapters.inadpt.purchase_api import purchase_repo
from pythonProject.app.adapters.out.mock_user_repository import MockUserRepository
from pythonProject.app.domain.use_cases.add_purchase_to_user import AddPurchaseToUser
from pythonProject.app.domain.use_cases.user_crud_use_case import UserCrudUseCase

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

user_router = APIRouter()

user_repo = MockUserRepository()
purchase_repo = purchase_repo
user_crud = UserCrudUseCase(user_repo)
add_purchases_use_case = AddPurchaseToUser(user_repo, purchase_repo)


@user_router.post("/user", response_model=UserResponseDTO)
def create_user(user_data: UserCreateDTO):
    new_user = user_crud.create_user(user_data.user, user_data.password)
    return new_user


@user_router.get("/user/{user_id}", response_model=UserResponseDTO)
def get_user(user_id: int):
    user = user_crud.get_user(user_id)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")


@user_router.put("/user/{user_id}", response_model=UserResponseDTO)
def update_user(user_id: int, user_data: UserCreateDTO):
    updated_user = user_crud.update_user(user_id, user_data.user, user_data.password)
    if updated_user:
        return updated_user
    raise HTTPException(status_code=404, detail="User not found")


@user_router.delete("/user/{user_id}")
def delete_user(user_id: int):
    if user_crud.delete_user(user_id):
        return {"detail": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")


@user_router.post("/user/purchase/{purchase_id}", response_model=UserResponseDTO)
def add_purchase_to_user(purchase_id: int):
    # Add the purchase to the user
    if add_purchases_use_case.execute(purchase_id):
        # Fetch the updated user data
        # Fetch the updated user data
        purchase = purchase_repo.read(purchase_id)
        user = user_crud.get_user(purchase.id_user)

        # Make sure purchases are converted to PurchaseResponseDTO objects, not User objects
        user.purchases = [PurchaseResponseDTO.from_orm(purchase) for purchase in user.purchases]

        return user
    raise HTTPException(status_code=404, detail="User not found")

