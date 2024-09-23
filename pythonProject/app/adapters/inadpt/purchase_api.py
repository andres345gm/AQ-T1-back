from typing import List
from fastapi import HTTPException, APIRouter

from pythonProject.app.adapters.DTOs.purchase_create_dto import PurchaseCreateDTO
from pythonProject.app.adapters.DTOs.purchase_response_dto import PurchaseResponseDTO
from pythonProject.app.adapters.out.mongo_purchase_repository import MongoPurchaseRepository
from pythonProject.app.domain.use_cases.purchase_crud_use_case import PurchaseCrudUseCase
from pythonProject.app.domain.use_cases.add_purchase_to_user import AddPurchaseToUser

purchase_router = APIRouter()

# Configuración de MongoDB
mongo_uri = "mongodb+srv://juanjogomezarenas1:pass12345@pokeapi.cjeck.mongodb.net/?retryWrites=true&w=majority&appName=pokeApi"
db_name = "pokedex_db"
purchase_repo = MongoPurchaseRepository(mongo_uri, db_name)
purchase_crud = PurchaseCrudUseCase(purchase_repo)

# Aquí también puedes inicializar el repositorio de usuarios si es necesario
from pythonProject.app.adapters.out.mongo_user_repository import MongoUserRepository

user_repo = MongoUserRepository(mongo_uri, db_name)
add_purchases_use_case = AddPurchaseToUser(user_repo, purchase_repo)


@purchase_router.post("/purchase", response_model=PurchaseResponseDTO)
def create_purchase(purchase_data: PurchaseCreateDTO):
    new_purchase = purchase_crud.create_purchase(
        purchase_data.id_pokemon, 
        purchase_data.date, 
        purchase_data.price, 
        purchase_data.id_user
    )
    if new_purchase is None:
        raise HTTPException(status_code=404, detail="Purchase not created")
    return new_purchase


@purchase_router.get("/purchase/{purchase_id}", response_model=PurchaseResponseDTO)
def get_purchase(purchase_id: str):  # Cambiado a str para ObjectId
    purchase = purchase_crud.get_purchase(purchase_id)
    if purchase:
        return purchase
    raise HTTPException(status_code=404, detail="Purchase not found")


@purchase_router.put("/purchase/{purchase_id}", response_model=PurchaseResponseDTO)
def update_purchase(purchase_id: str, purchase_data: PurchaseCreateDTO):  # Cambiado a str para ObjectId
    updated_purchase = purchase_crud.update_purchase(
        purchase_id, 
        purchase_data.id_pokemon, 
        purchase_data.date, 
        purchase_data.price, 
        purchase_data.id_user
    )
    if updated_purchase:
        return updated_purchase
    raise HTTPException(status_code=404, detail="Purchase not found")


@purchase_router.delete("/purchase/{purchase_id}")
def delete_purchase(purchase_id: str):  # Cambiado a str para ObjectId
    if purchase_crud.delete_purchase(purchase_id):
        return {"detail": "Purchase deleted"}
    raise HTTPException(status_code=404, detail="Purchase not found")


@purchase_router.get("/purchase", response_model=List[PurchaseResponseDTO])
def list_purchases():
    return purchase_crud.list_purchases()


@purchase_router.get("/purchase/user/{user_id}", response_model=List[PurchaseResponseDTO])
def list_purchases_user(user_id: int):
    return purchase_crud.list_purchases_user(user_id)


@purchase_router.post("/purchase/user", response_model=PurchaseResponseDTO)
def create_purchase_for_user(purchase_data: PurchaseCreateDTO):
    new_purchase = purchase_crud.create_purchase(
        purchase_data.id_pokemon, 
        purchase_data.date, 
        purchase_data.price, 
        purchase_data.id_user
    )
    if new_purchase is None:
        raise HTTPException(status_code=404, detail="Purchase not created")
    if add_purchases_use_case.execute(new_purchase.id):
        return new_purchase
    raise HTTPException(status_code=404, detail="Purchase not created")
