from abc import ABC, abstractmethod
from typing import List, Optional
from pythonProject.app.domain.model.user import User


class IUserRepository(ABC):
    @abstractmethod
    def create(self, user: User) -> User:
        pass
    
    @abstractmethod
    def read(self, user_id: int) -> Optional[User]:
        pass

    @abstractmethod
    def update(self, user_id: int, user: User) -> Optional[User]:
        pass

    @abstractmethod
    def delete(self, user_id: int) -> bool:
        pass

    @abstractmethod
    def list(self) -> List[User]:
        pass
