from pymongo import MongoClient

from pythonProject.app.domain.model.purchase import Purchase
from pythonProject.app.domain.model.user import User
from pythonProject.app.domain.use_cases.repositories.user_repository import IUserRepository

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MongoUserRepository(IUserRepository):
    def __init__(self, mongo_uri: str, db_name: str):
        self.client = MongoClient(mongo_uri)
        self.db = self.client[db_name]
        self.collection = self.db['user_collection']

    def get_next_id(self) -> int:
        # Get the total number of documents in the collection
        count = self.collection.count_documents({})
        # Add 1 to the current count to set the new ID
        return count + 1

    def create(self, user: User) -> User:
        user_dict = user.__dict__
        next_id = self.get_next_id()
        user_dict['_id'] = next_id
        user_dict['id'] = next_id

        # Convert purchases to dictionaries before inserting into MongoDB
        if 'purchases' in user_dict:
            user_dict['purchases'] = [purchase.to_dict() for purchase in user.purchases]

        result = self.collection.insert_one(user_dict)
        user.id = user_dict['_id']
        return user

    def read(self, user_id: int) -> User:
        logger.info(f"Fetching user with id {user_id}")
        user_data = self.collection.find_one({"_id": int(user_id)})
        if user_data is not None:
            user_data.pop('_id', None)

            # Convert purchases from dictionaries to Purchase objects
            if 'purchases' in user_data:
                user_data['purchases'] = [Purchase(**purchase) for purchase in user_data['purchases']]

            logger.info(f"User data: {user_data}")
            return User(**user_data)
        return None

    def update(self, user_id: int, user: User) -> User:
        # Convert purchases to dictionaries before updating in MongoDB
        user_dict = user.__dict__
        if 'purchases' in user_dict:
            user_dict['purchases'] = [purchase.to_dict() for purchase in user.purchases]

        self.collection.update_one({"_id": user_id}, {"$set": user_dict})
        return user

    def delete(self, user_id: int) -> bool:
        result = self.collection.delete_one({"_id": user_id})
        return result.deleted_count > 0

    def list(self) -> list:
        users = self.collection.find()
        return [User(**user) for user in users]

    def get_user_by_username(self, username: str) -> User:
        user_data = self.collection.find_one({"username": username})
        return User(**user_data) if user_data else None
