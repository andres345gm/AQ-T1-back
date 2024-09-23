from pymongo import MongoClient
from bson.objectid import ObjectId
from pythonProject.app.domain.model.user import User
from pythonProject.app.domain.use_cases.repositories.user_repository import IUserRepository

class MongoUserRepository(IUserRepository):
    def __init__(self, mongo_uri: str, db_name: str):
        self.client = MongoClient(mongo_uri)
        self.db = self.client[db_name]
        self.collection = self.db['user_collection']

    def create(self, user: User) -> User:
        user_dict = user.__dict__
        result = self.collection.insert_one(user_dict)
        user.id = str(result.inserted_id)
        return user

    def read(self, user_id: str) -> User:
        user_data = self.collection.find_one({"_id": ObjectId(user_id)})
        return User(**user_data) if user_data else None

    def update(self, user_id: str, user: User) -> User:
        self.collection.update_one({"_id": ObjectId(user_id)}, {"$set": user.__dict__})
        return user

    def delete(self, user_id: str) -> bool:
        result = self.collection.delete_one({"_id": ObjectId(user_id)})
        return result.deleted_count > 0

    def list(self) -> list:
        users = self.collection.find()
        return [User(**user) for user in users]

    def get_user_by_username(self, username: str) -> User:
        user_data = self.collection.find_one({"username": username})
        return User(**user_data) if user_data else None
