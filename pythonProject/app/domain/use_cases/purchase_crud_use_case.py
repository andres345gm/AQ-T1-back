from typing import List, Optional

from pythonProject.app.domain.model.purchase import Purchase
from pythonProject.app.domain.use_cases.repositories.purchase_repository import IPurchaseRepository


class PurchaseCrudUseCase:
    def __init__(self, purchase_repo: IPurchaseRepository):
        self.purchase_repo = purchase_repo

    def create_purchase(self, pokemon_id: id, date: str, price: int, id_user) -> Purchase:
        purchase = Purchase(0, pokemon_id, date, price, id_user)
        return self.purchase_repo.create(purchase)

    def get_purchase(self, purchase_id: int) -> Optional[Purchase]:
        return self.purchase_repo.read(purchase_id)

    def update_purchase(self, purchase_id: int, pokemon_id: id, date: str, price: int, id_user) -> Optional[Purchase]:
        purchase = Purchase(purchase_id, pokemon_id, date, price, id_user)
        return self.purchase_repo.update(purchase_id, purchase)

    def delete_purchase(self, purchase_id: int) -> bool:
        return self.purchase_repo.delete(purchase_id)

    def list_purchases(self) -> List[Purchase]:
        return self.purchase_repo.list()
