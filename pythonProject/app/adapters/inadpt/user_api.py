import logging
from typing import List

from fastapi import HTTPException, APIRouter

from pythonProject.app.adapters.DTOs.purchase_response_dto import PurchaseResponseDTO
from pythonProject.app.adapters.DTOs.user_create_dto import UserCreateDTO
from pythonProject.app.adapters.DTOs.user_response_dto import UserResponseDTO
from pythonProject.app.adapters.out.mongo_user_repository import MongoUserRepository
from pythonProject.app.domain.use_cases.add_purchase_to_user import AddPurchaseToUser
from pythonProject.app.domain.use_cases.user_crud_use_case import UserCrudUseCase

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

user_router = APIRouter()

# Configuración de MongoDB
mongo_uri = "mongodb+srv://juanjogomezarenas1:pass12345@pokeapi.cjeck.mongodb.net/?retryWrites=true&w=majority&appName=pokeApi"
db_name = "pokedex_db"
user_repo = MongoUserRepository(mongo_uri, db_name)
user_crud = UserCrudUseCase(user_repo)

# Puedes reutilizar el repositorio de compras aquí
from pythonProject.app.adapters.out.mongo_purchase_repository import MongoPurchaseRepository

purchase_repo = MongoPurchaseRepository(mongo_uri, db_name)
add_purchases_use_case = AddPurchaseToUser(user_repo, purchase_repo)


@user_router.post("/user", response_model=UserResponseDTO)
def create_user(user_data: UserCreateDTO):
    new_user = user_crud.create_user(user_data.user, user_data.password)
    return new_user


@user_router.get("/user/{user_id}", response_model=UserResponseDTO)
def get_user(user_id: str):  # Cambiado a str para ObjectId
    user = user_crud.get_user(user_id)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")


@user_router.put("/user/{user_id}", response_model=UserResponseDTO)
def update_user(user_id: str, user_data: UserCreateDTO):  # Cambiado a str para ObjectId
    updated_user = user_crud.update_user(user_id, user_data.user, user_data.password)
    if updated_user:
        return updated_user
    raise HTTPException(status_code=404, detail="User not found")


@user_router.delete("/user/{user_id}")
def delete_user(user_id: str):  # Cambiado a str para ObjectId
    if user_crud.delete_user(user_id):
        return {"detail": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")


@user_router.post("/user/purchase/{purchase_id}", response_model=UserResponseDTO)
def add_purchase_to_user(purchase_id: str):  # Cambiado a str para ObjectId
    if add_purchases_use_case.execute(purchase_id):
        purchase = purchase_repo.read(purchase_id)
        user = user_crud.get_user(purchase.id_user)

        # Asegúrate de que las compras se conviertan a objetos PurchaseResponseDTO
        user.purchases = [PurchaseResponseDTO.from_orm(purchase) for purchase in user.purchases]

        return user
    raise HTTPException(status_code=404, detail="User not found")
