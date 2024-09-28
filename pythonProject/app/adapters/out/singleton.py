from pythonProject.app.adapters.out.mongo_purchase_repository import MongoPurchaseRepository
from pythonProject.app.adapters.out.mongo_user_repository import MongoUserRepository

uri = "mongodb+srv://juanjogomezarenas1:pass12345@pokeapi.cjeck.mongodb.net/?retryWrites=true&w=majority&appName=pokeApi"
db_name = "pokedex_db"
singletonUserRepository = MongoUserRepository(uri, db_name)
singletonPurchaseRepository = MongoPurchaseRepository(uri, db_name)