from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.model.user import User


class IUserRepository(ABC):
    @abstractmethod
    def create(self, user: User) -> User:
        pass
    
    @abstractmethod
    def read(self, user_id: str) -> Optional[User]:
        pass

    @abstractmethod
    def update(self, user_id: str, user: User) -> Optional[User]:
        pass

    @abstractmethod
    def delete(self, user_id: str) -> bool:
        pass

    @abstractmethod
    def list(self) -> List[User]:
        pass
