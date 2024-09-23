from pymongo import MongoClient
from bson.objectid import ObjectId
from pythonProject.app.domain.model.purchase import Purchase
from pythonProject.app.domain.model.user import User
from pythonProject.app.domain.use_cases.repositories.purchase_repository import IPurchaseRepository


class MongoPurchaseRepository(IPurchaseRepository):
    def __init__(self, mongo_uri: str, db_name: str):
        self.client = MongoClient(mongo_uri)
        self.db = self.client[db_name]
        self.collection = self.db['purchase_collection']

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

    def read(self, purchase_id: str) -> Purchase:
        purchase_data = self.collection.find_one({"_id": ObjectId(purchase_id)})
        return Purchase(**purchase_data) if purchase_data else None

    def update(self, purchase_id: str, purchase: Purchase) -> Purchase:
        self.collection.update_one({"_id": ObjectId(purchase_id)}, {"$set": purchase.__dict__})
        return purchase

    def delete(self, purchase_id: str) -> bool:
        result = self.collection.delete_one({"_id": ObjectId(purchase_id)})
        return result.deleted_count > 0

    def list(self) -> list:
        purchases = self.collection.find()
        return [Purchase(**purchase) for purchase in purchases]

    def list_purchases_user(self, user_id: int) -> list:
        purchases = self.collection.find({"id_user": user_id})
        return [Purchase(**purchase) for purchase in purchases]
