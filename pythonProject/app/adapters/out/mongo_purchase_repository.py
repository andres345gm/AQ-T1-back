from pymongo import MongoClient
from bson.objectid import ObjectId
from pythonProject.app.domain.model.purchase import Purchase
from pythonProject.app.domain.use_cases.repositories.purchase_repository import IPurchaseRepository

class MongoPurchaseRepository(IPurchaseRepository):
    def __init__(self, mongo_uri: str, db_name: str):
        self.client = MongoClient(mongo_uri)
        self.db = self.client[db_name]
        self.collection = self.db['purchase_collection']

    def create(self, purchase: Purchase) -> Purchase:
        purchase_dict = purchase.__dict__
        result = self.collection.insert_one(purchase_dict)
        purchase.id = str(result.inserted_id)
        return purchase

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
