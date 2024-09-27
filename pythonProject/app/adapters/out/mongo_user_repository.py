from pymongo import MongoClient
from pythonProject.app.domain.model.purchase import Purchase
from pythonProject.app.domain.model.user import User
from pythonProject.app.domain.ports.user_repository import IUserRepository
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MongoUserRepository(IUserRepository):
    def __init__(self, mongo_uri: str, db_name: str):
        self.client = MongoClient(mongo_uri)
        self.db = self.client[db_name]
        self.collection = self.db['user_collection']

    def get_next_id(self) -> int:
        count = self.collection.count_documents({})
        return count + 1

    def create(self, user: User) -> User:
        user_dict = user.__dict__.copy()
        next_id = self.get_next_id()
        user_dict['_id'] = next_id
        user.id_ = next_id

        if 'purchases' in user_dict:
            user_dict['purchases'] = [purchase.to_dict() for purchase in user.purchases]

        user_dict.pop('id_', None)
        self.collection.insert_one(user_dict)
        return user

    def read(self, user_id: int) -> User:
        logger.info(f"Fetching user with _id: {user_id}")
        user_data = self.collection.find_one({"_id": user_id})

        if user_data is not None:
            user_id_value = user_data.pop('_id')
            return User(id=user_id_value, **user_data)

        return None

    def update(self, user_id: int, user: User) -> User:
        user_dict = {
            "user": user.user,
            "password": user.password,
            "balance": user.balance,
            "purchases": [purchase.to_dict() for purchase in user.purchases] if user.purchases else []
        }

        self.collection.update_one({"_id": user_id}, {"$set": user_dict})
        user.id_ = user_id
        return user

    def delete(self, user_id: int) -> bool:
        result = self.collection.delete_one({"_id": user_id})
        return result.deleted_count > 0

    def list(self) -> list:
        users = self.collection.find()
        return [User(id=user['_id'], **user) for user in users]

    def get_user_by_username(self, username: str) -> User:
        user_data = self.collection.find_one({"user": username})  # Asegúrate de usar el campo correcto
        if user_data:
            user_id_value = user_data.pop('_id')
            return User(id=user_id_value, **user_data)
        return None
