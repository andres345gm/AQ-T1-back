from pythonProject.app.domain.model.user import User
from pythonProject.app.domain.use_cases.repositories.user_repository import IUserRepository


class MockUserRepository(IUserRepository):
    def __init__(self):
        self.users = {
            1: User(1, "user1", "password1"),
            2: User(2, "user2", "password2")
        }

    def create(self, user: User) -> User:
        user.id = max(self.users.keys()) + 1
        self.users[user.id] = user
        return user

    def read(self, user_id: int) -> User:
        return self.users.get(user_id)

    def update(self, user_id: int, user: User) -> User:
        if user_id in self.users:
            self.users[user_id] = user
            return user
        return None

    def delete(self, user_id: int) -> bool:
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False

    def list(self) -> list:
        return list(self.users.values())

    def get_user_by_username(self, username: str) -> User:
        for user in self.users.values():
            if user.user == username:
                return user
        return None