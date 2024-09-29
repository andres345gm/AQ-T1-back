from typing import List, Optional
from app.domain.model.user import User
from app.domain.ports.user_repository import IUserRepository

class UserCrudUseCase:
    def __init__(self, user_repo: IUserRepository):
        self.user_repo = user_repo

    def create_user(self, username: str, password: str) -> User:
        user = User(0, username, password)
        return self.user_repo.create(user)

    def get_user(self, user_id: int) -> Optional[User]:
        return self.user_repo.read(user_id)

    def update_user(self, user_id: int, username: str, password: str) -> Optional[User]:
        user = User(user_id, username, password)
        return self.user_repo.update(user_id, user)

    def delete_user(self, user_id: int) -> bool:
        return self.user_repo.delete(user_id)

    def list_users(self) -> List[User]:
        return self.user_repo.list()
