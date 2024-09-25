import logging

from fastapi import HTTPException, APIRouter

from pythonProject.app.adapters.DTOs.purchase_create_dto import PurchaseCreateDTO, map_dto_to_purchase
from pythonProject.app.adapters.DTOs.user_create_dto import UserCreateDTO
from pythonProject.app.adapters.DTOs.user_response_dto import UserResponseDTO, map_user_to_response_dto
from pythonProject.app.adapters.out.singleton import singletonUserRepository, singletonPurchaseRepository
from pythonProject.app.domain.model.user import User
from pythonProject.app.domain.use_cases.add_purchase_to_user import AddPurchaseToUser
from pythonProject.app.domain.use_cases.user_crud_use_case import UserCrudUseCase

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

user_router = APIRouter()

# Configuración de MongoDB
#mongo_uri = "mongodb+srv://juanjogomezarenas1:pass12345@pokeapi.cjeck.mongodb.net/?retryWrites=true&w=majority&appName=pokeApi&tlsAllowInvalidCertificates=true"
#db_name = "pokedex_db"
#user_repo = MongoUserRepository(mongo_uri, db_name)
user_crud = UserCrudUseCase(singletonUserRepository)
add_purchases_use_case = AddPurchaseToUser(singletonUserRepository, singletonPurchaseRepository)


# Puedes reutilizar el repositorio de compras aquí

#purchase_repo = MongoPurchaseRepository(mongo_uri, db_name)
#add_purchases_use_case = AddPurchaseToUser(user_repo, purchase_repo)


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
def get_user(user_id: int):  # Cambiado a str para ObjectId
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
