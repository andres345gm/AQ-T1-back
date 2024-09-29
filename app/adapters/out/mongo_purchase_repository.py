from app.domain.model.purchase import Purchase
from app.domain.ports.purchase_repository import IPurchaseRepository
from pymongo import MongoClient


class MongoPurchaseRepository(IPurchaseRepository):
    def __init__(self, mongo_uri: str, db_name: str):
        self.client = MongoClient(mongo_uri)
        self.db = self.client[db_name]
        self.collection = self.db['user_collection']  # Se almacenan las compras en los documentos de usuarios

    def create(self, purchase: Purchase) -> Purchase:
        # Generar un ID para la compra
        purchase.id_ = self.get_next_purchase_id(purchase.id_user)
        purchase_dict = purchase.to_dict()

        # Insertar la compra en la lista de compras del usuario
        self.collection.update_one(
            {"_id": purchase.id_user},
            {"$push": {"purchases": purchase_dict}}
        )

        return purchase

    def read(self, purchase_id: int) -> Purchase:
        # Buscar la compra dentro de la lista de compras de los usuarios
        user = self.collection.find_one(
            {"purchases.id": purchase_id},
            {"purchases.$": 1}  # Solo devuelve la compra que coincide
        )

        if user and 'purchases' in user:
            purchase_data = user['purchases'][0]  # La compra está en la posición 0
            return Purchase(**purchase_data)
        
        return None

    def update(self, purchase_id: int, purchase: Purchase) -> Purchase:
        # Actualizar una compra específica dentro de la lista de compras del usuario
        self.collection.update_one(
            {"purchases.id": purchase_id},
            {"$set": {"purchases.$": purchase.to_dict()}}
        )
        
        return purchase

    def delete(self, purchase_id: int) -> bool:
        # Eliminar una compra de la lista de compras del usuario
        result = self.collection.update_one(
            {"purchases.id": purchase_id},
            {"$pull": {"purchases": {"id": purchase_id}}}
        )
        return result.modified_count > 0

    def list(self) -> list:
        # Devolver todas las compras de todos los usuarios
        users = self.collection.find({}, {"purchases": 1})
        purchases = []

        for user in users:
            purchases.extend(user.get("purchases", []))

        return [Purchase(**purchase) for purchase in purchases]

    def list_purchases_user(self, user_id: int) -> list:
        # Buscar todas las compras de un usuario específico
        user = self.collection.find_one({"_id": user_id}, {"purchases": 1})

        if user and 'purchases' in user:
            return [Purchase(**purchase) for purchase in user['purchases']]
        return []

    def get_next_purchase_id(self, user_id: int) -> int:
        # Obtener el siguiente ID de compra en función de las compras actuales del usuario
        user = self.collection.find_one({"_id": user_id}, {"purchases": 1})
        if user and 'purchases' in user and user['purchases']:
            max_id = max(purchase['id'] for purchase in user['purchases'])
            return max_id + 1
        return 1
