import logging
from typing import List

from fastapi import HTTPException, APIRouter

from pythonProject.app.adapters.DTOs.purchase_create_dto import PurchaseCreateDTO, map_dto_to_purchase
from pythonProject.app.adapters.DTOs.purchase_response_dto import PurchaseResponseDTO, map_purchase_to_dto
from pythonProject.app.adapters.out.singleton import singletonPurchaseRepository, singletonUserRepository
from pythonProject.app.domain.use_cases.add_purchase_to_user import AddPurchaseToUser
from pythonProject.app.domain.use_cases.purchase_crud_use_case import PurchaseCrudUseCase

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
purchase_router = APIRouter()

# Configuración de MongoDB
# mongo_uri = "mongodb+srv://juanjogomezarenas1:pass12345@pokeapi.cjeck.mongodb.net/?retryWrites=true&w=majority&appName=pokeApi"
# db_name = "pokedex_db"
# purchase_repo = MongoPurchaseRepository(mongo_uri, db_name)
purchase_crud = PurchaseCrudUseCase(singletonPurchaseRepository)

# Aquí también puedes inicializar el repositorio de usuarios si es necesario
# from pythonProject.app.adapters.out.mongo_user_repository import MongoUserRepository

#user_repo = MongoUserRepository(mongo_uri, db_name)

add_purchases_use_case = AddPurchaseToUser(singletonUserRepository, singletonPurchaseRepository)


@purchase_router.post("/purchase/user", response_model=PurchaseResponseDTO)
def create_purchase(purchase_data: PurchaseCreateDTO):
    new_purchase = map_dto_to_purchase(purchase_data)
    new_purchase_created = purchase_crud.create_purchase(
        new_purchase.id_pokemon,
        new_purchase.date,
        new_purchase.price,
        new_purchase.id_user
    )
    if new_purchase_created is None:
        raise HTTPException(status_code=404, detail="Purchase not created")
    new_purchase_response = map_purchase_to_dto(new_purchase_created)
    logger.info(f"Purchase created with id {new_purchase_response.id}")
    return new_purchase_response


@purchase_router.get("/purchase/{purchase_id}", response_model=PurchaseResponseDTO)
def get_purchase(purchase_id: int):  # Cambiado a str para ObjectId
    purchase = purchase_crud.get_purchase(purchase_id)
    if purchase:
        new_purchase_response = map_purchase_to_dto(purchase)
        return new_purchase_response
    raise HTTPException(status_code=404, detail="Purchase not found")


@purchase_router.put("/purchase/{purchase_id}", response_model=PurchaseResponseDTO)
def update_purchase(purchase_id: int, purchase_data: PurchaseCreateDTO):  # Cambiado a str para ObjectId
    updated_purchase = purchase_crud.update_purchase(
        purchase_id,
        purchase_data.id_pokemon,
        purchase_data.date,
        purchase_data.price,
        purchase_data.id_user
    )
    if updated_purchase:
        updated_purchase_response = map_purchase_to_dto(updated_purchase)
        return updated_purchase_response
    raise HTTPException(status_code=404, detail="Purchase not found")


@purchase_router.delete("/purchase/{purchase_id}")
def delete_purchase(purchase_id: int):  # Cambiado a str para ObjectId
    if purchase_crud.delete_purchase(purchase_id):
        return {"detail": "Purchase deleted"}
    raise HTTPException(status_code=404, detail="Purchase not found")


@purchase_router.get("/purchase/user/{user_id}", response_model=List[PurchaseResponseDTO])
def list_purchases_user(user_id: int):
    purchases_list = purchase_crud.list_purchases_user(user_id)
    purchases_response_list = [map_purchase_to_dto(purchase) for purchase in purchases_list]
    return purchases_response_list
