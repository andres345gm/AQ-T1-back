import datetime
from pythonProject.app.domain.model.purchase import Purchase
from pythonProject.app.domain.model.user import User
from pythonProject.app.domain.use_cases.repositories.user_repository import IUserRepository


class MockUserRepository(IUserRepository):
    def __init__(self):
        self.users = {
            1: self.create_user_with_purchase(1, "user1", "password1"),
            2: User(2, "user2", "password2")
        }

    def create_user_with_purchase(self, id: int, user: str, password: str):
        user_instance = User(id, user, password)
        # Crea una compra predefinida
        purchase = Purchase(1, 703, "11/10/2021", 1, id)  # ID de compra, ID del Pokémon, fecha, precio, ID del usuario
        user_instance.add_purchase(purchase)
        return user_instance

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