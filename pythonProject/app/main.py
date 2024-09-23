from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pythonProject.app.adapters.inadpt.login_api import login_router
from pythonProject.app.adapters.inadpt.poke_api import poke_router
from pythonProject.app.adapters.inadpt.purchase_api import purchase_router
from pythonProject.app.adapters.inadpt.user_api import user_router
from pythonProject.app.adapters.out.mongo_purchase_repository import MongoPurchaseRepository
from pythonProject.app.adapters.out.mongo_user_repository import MongoUserRepository

app = FastAPI()

# Configuración de MongoDB
mongo_uri = "mongodb+srv://juanjogomezarenas1:pass12345@pokeapi.cjeck.mongodb.net/?retryWrites=true&w=majority&appName=pokeApi"
db_name = "pokedex_db"

# Inicialización de repositorios
purchase_repo = MongoPurchaseRepository(mongo_uri, db_name)
user_repo = MongoUserRepository(mongo_uri, db_name)

# Aquí deberías crear los casos de uso pasando los repositorios
from pythonProject.app.domain.use_cases.purchase_crud_use_case import PurchaseCrudUseCase
from pythonProject.app.domain.use_cases.user_crud_use_case import UserCrudUseCase
from pythonProject.app.domain.use_cases.add_purchase_to_user import AddPurchaseToUser

purchase_crud = PurchaseCrudUseCase(purchase_repo)
user_crud = UserCrudUseCase(user_repo)
add_purchases_use_case = AddPurchaseToUser(user_repo, purchase_repo)

# Incluir los routers
app.include_router(purchase_router)
app.include_router(login_router)
app.include_router(user_router)
app.include_router(poke_router)

# Configuración de CORS
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"data": "This API manages your own pokemon collection!"}
