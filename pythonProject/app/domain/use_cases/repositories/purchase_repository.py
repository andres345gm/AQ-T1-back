from abc import ABC, abstractmethod
from typing import List, Optional
from pythonProject.app.domain.model.purchase import Purchase


class IPurchaseRepository(ABC):
    @abstractmethod
    def create(self, purchase: Purchase) -> Purchase:
        pass

    @abstractmethod
    def read(self, purchase_id: int) -> Optional[Purchase]:
        pass

    @abstractmethod
    def update(self, purchase_id: int, purchase: Purchase) -> Optional[Purchase]:
        pass

    @abstractmethod
    def delete(self, purchase_id: int) -> bool:
        pass

    @abstractmethod
    def list(self) -> List[Purchase]:
        pass
