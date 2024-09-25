from pythonProject.app.domain.model.purchase import Purchase
from pythonProject.app.domain.use_cases.repositories.purchase_repository import IPurchaseRepository


class MockPurchaseRepository(IPurchaseRepository):
    def __init__(self):
        self.purchases = {
            1: Purchase(1, 1, "10/10/2021", 1, 1),
            2: Purchase(2, 4, "11/10/2021", 1, 1),
            3: Purchase(3, 2, "12/10/2021", 2, 2)  # Ejemplo de otra compra
        }

    def create(self, purchase: Purchase) -> Purchase:
        purchase.id_ = max(self.purchases.keys()) + 1
        self.purchases[purchase.id_] = purchase
        return purchase

    def read(self, purchase_id: int) -> Purchase:
        return self.purchases.get(purchase_id)

    def update(self, purchase_id: int, purchase: Purchase) -> Purchase:
        if purchase_id in self.purchases:
            self.purchases[purchase_id] = purchase
            return purchase
        return None

    def delete(self, purchase_id: int) -> bool:
        if purchase_id in self.purchases:
            del self.purchases[purchase_id]
            return True
        return False

    def list(self) -> list:
        return list(self.purchases.values())
    
    def list_purchases_user(self, user_id: int) -> list:
        # Filtrar compras según el id_user
        return [purchase for purchase in self.purchases.values() if purchase.id_user == user_id]
